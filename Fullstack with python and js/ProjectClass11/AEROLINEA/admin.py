from django.contrib import admin
from .models import Aeropuerto, Pasajero, Vuelo

# Register your models here.
admin.site.register(Vuelo)
admin.site.register(Aeropuerto)
admin.site.register(Pasajero)