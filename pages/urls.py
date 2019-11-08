from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1/', views.index1, name='index1'),
    path('lk/', views.lk, name='lk'),
    path('search/', views.search, name='search')



]