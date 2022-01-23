from django.urls import path

from .views import SerializedProjectsView, SerializedProjectFiltersView

urlpatterns = [
    path('project_filters/', SerializedProjectFiltersView.as_view(), name='project_filters'),
    path('projects/', SerializedProjectsView.as_view(), name='projects'),
]
