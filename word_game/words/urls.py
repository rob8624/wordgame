from . import views

from django.urls import path

urlpatterns = [
    path('', views.homeView, name='home'),#this is the home url
    path('search', views.searchView, name='search'),#this is the search url
]