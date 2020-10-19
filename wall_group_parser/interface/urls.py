from django.urls import path


from . import views


urlpatterns = [
    path('', views.AboutPageView.as_view() ,name='about_page'),
    path('search/', views.SearchGroupView.as_view(), name='search_page')
]
