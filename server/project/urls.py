"""project urls."""
from django.urls import path, re_path

from project.views import ProjectListView, ProjectDetailView

app_name = 'project'

urlpatterns = [
    path('', ProjectListView.as_view(), name='index'),
    re_path(r'(?P<uid>\w+)/', ProjectDetailView.as_view(), name='detail'),
]
