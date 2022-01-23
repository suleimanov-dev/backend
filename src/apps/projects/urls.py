from django.urls import path

from .views import SerializedProjectsView

urlpatterns = [
    path('projects/', SerializedProjectsView.as_view(), name='projects'),
]
