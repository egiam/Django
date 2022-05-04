from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from idna import valid_contextj
from .models import Pasajero, Vuelo
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    pass

def index(request):
    return render(request, "vuelos/index.html", {
        "lista_vuelos": Vuelo.objects.all()
    })

def vuelo(request, vuelo_id):
    vuelo = Vuelo.objects.get(id = vuelo_id)
    pasajeros = vuelo.pasajeros.all()
    no_son_pasajeros = Pasajero.objects.exclude(vuelos=vuelo).all()
    return render(request, "vuelos/vuelo.html", {
        "vuelo": vuelo,
        "pasajeros": pasajeros,
        "no_son_pasajeros": no_son_pasajeros
    })

def reserva(request, vuelo_id):
    if request.method == "POST":
        vuelo = Vuelo.objects.get(pk=vuelo_id)
        pasajero_id = int(request.POST["pasajero"])
        pasajero = Pasajero.objects.get(pk=pasajero_id)
        pasajero.vuelos.add(vuelo)
        return HttpResponseRedirect(reverse("AEROLINEA:vuelo", args=(vuelo.id)))

