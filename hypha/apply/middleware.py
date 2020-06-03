from wagtail.core.models import Site

from .home.models import ApplyHomePage


def apply_url_conf_middleware(get_response):
    # If we are on a page which belongs to the same site as an ApplyHomePage
    # we change the url conf to one that includes links to all the logged
    # in functionality. Login and Logout are included with the global package
    # of urls
    def middleware(request):
        site = Site.find_for_request(request)
        homepage = site.root_page.specific
        if isinstance(homepage, ApplyHomePage):
            request.urlconf = 'hypha.apply.urls'

        response = get_response(request)
        return response

    return middleware
