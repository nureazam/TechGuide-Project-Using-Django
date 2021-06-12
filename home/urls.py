from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("website", views.website, name='website'),
    path("game", views.game, name='game'),
    path("apks", views.apks, name='apks'),
]
