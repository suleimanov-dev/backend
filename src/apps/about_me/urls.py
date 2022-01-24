from django.urls import path

from .views import SerializedMainInfoView, SerializedTimelineView

urlpatterns = [
    path('api/about_me/main_info/', SerializedMainInfoView.as_view(), name='main_info'),
    path('api/about_me/timeline/', SerializedTimelineView.as_view(), name='timeline'),
]
