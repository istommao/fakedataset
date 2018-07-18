"""project views."""
from django.views import generic

from project.models import Project


class ProjectListView(generic.TemplateView):

    view_name = 'project_index'
    template_name = 'project/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        projects = Project.objects.all()

        context.update({'projects': projects})
        return context


class ProjectDetailView(generic.TemplateView):

    view_name = 'project_detail'
    template_name = 'project/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uid = kwargs['uid']
        project = Project.objects.filter(uid=uid).first()

        context.update({'project': project})
        return context
