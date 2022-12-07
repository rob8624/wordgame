from . import views

from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),#this is the home url
    path('search', views.search_view, name='search'),#this is the search url
]