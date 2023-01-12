from django.contrib import admin
from django.urls import path,include
from DRF_App import views

urlpatterns = [
    path('', views.register.as_view(),name='register'),
]