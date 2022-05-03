from django.shortcuts import render
from .models import Vuelo

# Create your views here.
def index(request):
    pass

def index(request):
    return render(request, "vuelos/index.html", {
        "lista_vuelos": Vuelo.objects.all()
    })