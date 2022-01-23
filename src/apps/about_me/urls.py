from django.urls import path

from .views import SerializedMainInfoView

urlpatterns = [
    path('main_info/', SerializedMainInfoView.as_view(), name='main_info'),
]
