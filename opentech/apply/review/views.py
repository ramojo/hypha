import json

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from opentech.apply.activity.messaging import messenger, MESSAGES
from opentech.apply.funds.models import ApplicationSubmission
from opentech.apply.review.blocks import ScoreFieldBlock
from opentech.apply.review.forms import ReviewModelForm
from opentech.apply.review.options import RATE_CHOICE_NA, RATE_CHOICES_DICT
from opentech.apply.users.decorators import staff_required
from opentech.apply.utils.views import CreateOrUpdateView

from .models import Review


class ReviewContextMixin:
    def get_context_data(self, **kwargs):
        staff_reviews = self.object.reviews.by_staff()
        reviewer_reviews = self.object.reviews.by_reviewers().exclude(id__in=staff_reviews)
        return super().get_context_data(
            staff_reviews=staff_reviews,
            reviewer_reviews=reviewer_reviews,
            **kwargs,
        )


def get_form_for_stage(submission):
    forms = submission.page.specific.review_forms.all()
    index = submission.workflow.stages.index(submission.stage)
    return forms[index].form


class ReviewCreateOrUpdateView(CreateOrUpdateView):
    model = Review
    template_name = 'review/review_form.html'

    def get_object(self, queryset=None):
        return self.model.objects.get(submission=self.submission, author=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        self.submission = get_object_or_404(ApplicationSubmission, id=self.kwargs['submission_pk'])

        if not self.submission.phase.permissions.can_review(request.user) or not self.submission.has_permission_to_review(request.user):
            raise PermissionDenied()

        if self.request.POST and self.submission.reviewed_by(request.user):
            return self.get(request, *args, **kwargs)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        has_submitted_review = self.submission.reviewed_by(self.request.user)
        return super().get_context_data(
            submission=self.submission,
            has_submitted_review=has_submitted_review,
            title="Update Review draft" if self.object else 'Create Review',
            **kwargs
        )

    def get_form_class(self):
        return ReviewModelForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['submission'] = self.submission
        kwargs['review_form'] = get_form_for_stage(self.submission)

        if self.object:
            kwargs['initial'] = self.object.form_data
            kwargs['initial']['recommendation'] = self.object.recommendation

        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)

        if not self.object.is_draft:
            messenger(
                MESSAGES.NEW_REVIEW,
                request=self.request,
                user=self.object.author,
                submission=self.submission,
            )
        return response

    def get_success_url(self):
        return self.submission.get_absolute_url()


class ReviewDetailView(DetailView):
    model = Review

    def dispatch(self, request, *args, **kwargs):
        review = self.get_object()
        author = review.author

        if request.user != author and not request.user.is_superuser and request.user != review.submission.lead:
            raise PermissionDenied

        if review.is_draft:
            return HttpResponseRedirect(reverse_lazy('apply:reviews:form', args=(review.submission.id,)))

        return super().dispatch(request, *args, **kwargs)


@method_decorator(staff_required, name='dispatch')
class ReviewListView(ListView):
    model = Review

    def get_queryset(self):
        self.submission = get_object_or_404(ApplicationSubmission, id=self.kwargs['submission_pk'])
        self.queryset = self.model.objects.filter(submission=self.submission)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        review_data = {}

        for review in self.object_list:
            # Add the name header row
            review_data.setdefault('', []).append(str(review.author))
            review_data.setdefault('Score', []).append(str(review.score))

            for data, field in review.data_and_fields():
                title = field.value['field_label']
                review_data.setdefault(title, [])

                if isinstance(field.block, ScoreFieldBlock):
                    value = json.loads(data)
                    review_data.setdefault(title, []).append(str(value[0]))
                    review_data.setdefault(f'Rate {title}', [])

                    rating = int(value[1])
                    review_data.setdefault(f'Rate {title}', []).append(RATE_CHOICES_DICT.get(rating, RATE_CHOICE_NA))
                else:
                    review_data.setdefault(title, []).append(str(data))

        return super().get_context_data(
            submission=self.submission,
            review_data=review_data,
            **kwargs
        )
