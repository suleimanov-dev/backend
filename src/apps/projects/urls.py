from django.urls import path

from .views import SerializedProjectsView, SerializedProjectFiltersView, SerializedProjectView

urlpatterns = [
    path('api/projects/project_filters/', SerializedProjectFiltersView.as_view(), name='project_filters'),
    path('api/projects/projects/', SerializedProjectsView.as_view(), name='projects'),
    path('api/projects/projects/<name>/', SerializedProjectView.as_view(), name='project')
]
