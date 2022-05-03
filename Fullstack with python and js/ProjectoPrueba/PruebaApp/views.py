from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    return HttpResponse("Hola mundo!");

def harry (request):
    return HttpResponse("¡Hola Harry");

def hermione (request):
    return HttpResponse("¡Hola Hermione");

def hola(request, nombre):
    return HttpResponse(f"¡Hola, {nombre.capitalize()}!");

def plantilla (request):
    return render (request, "hola/index.html")

def saludar (request, nombre):
    return render (request, "hola/saludar.html", {
        "nombre" : nombre.capitalize()
    })