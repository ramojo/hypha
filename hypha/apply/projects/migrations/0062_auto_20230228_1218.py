# Generated by Django 3.2.18 on 2023-02-28 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('application_projects', '0061_remove_checks'),
    ]

    operations = [
        migrations.CreateModel(
            name='PAFApprovals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='pafreviewersrole',
            old_name='role',
            new_name='label',
        ),
        migrations.AddField(
            model_name='pafreviewersrole',
            name='user_roles',
            field=modelcluster.fields.ParentalManyToManyField(help_text="Only selected group's users will be listed for this PAFReviewerRole", related_name='paf_reviewers_roles', to='auth.Group', verbose_name='user groups'),
        ),
        migrations.DeleteModel(
            name='Approval',
        ),
        migrations.AddField(
            model_name='pafapprovals',
            name='paf_reviewer_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paf_approvals', to='application_projects.pafreviewersrole'),
        ),
        migrations.AddField(
            model_name='pafapprovals',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paf_approvals', to='application_projects.project'),
        ),
        migrations.AddField(
            model_name='pafapprovals',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paf_approvals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='pafapprovals',
            unique_together={('project', 'paf_reviewer_role')},
        ),
    ]
