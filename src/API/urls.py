from django.urls import path

from .views import GroupView, GetGroupView


urlpatterns = [
    path('group', GroupView.as_view()),
    path('group/<str:screen_name>', GetGroupView.as_view()),
]
