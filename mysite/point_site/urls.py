from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('send/', views.sendView, name='send'),
    path('generate/', views.generateView, name='generate')
]