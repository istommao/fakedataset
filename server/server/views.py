"""server views."""
from django.views import generic


class IndexView(generic.TemplateView):
    """Index view."""

    view_name = 'index'

    template_name = 'index.html'
