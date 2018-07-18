"""account views."""
from django.views import generic


class AccountView(generic.TemplateView):

    view_name = 'account_index'
    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
