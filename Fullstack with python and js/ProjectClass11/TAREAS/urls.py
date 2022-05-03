from django import views
from django.urls import path, include
from . import views

app_name = "TAREAS"
urlpatterns = [
    path('', views.index, name="index"),
    path('agregar', views.agregar, name="agregar"),
]