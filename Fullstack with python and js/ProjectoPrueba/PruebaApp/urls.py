from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('harry', views.harry, name="harry"),
    path('hermione', views.hermione, name="hermione"),
    path('<str:nombre>', views.hola, name="hola"),
    path('plantilla', views.plantilla, name="plantilla"),
    path('plantillasaludo/<str:nombre>', views.saludar, name="saludar"),
]