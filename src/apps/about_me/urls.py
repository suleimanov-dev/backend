from django.urls import path

from .views import SerializedMainInfoView, SerializedTimelineView

urlpatterns = [
    path('main_info/', SerializedMainInfoView.as_view(), name='main_info'),
    path('timeline/', SerializedTimelineView.as_view(), name='timeline')
]
