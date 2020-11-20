from django.urls import path

from .views import GroupView


urlpatterns = [
    path('group', GroupView.as_view()),
]
