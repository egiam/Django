from django.db import models

# Create your models here.

class Vuelo(models.Model):
    origen = models.CharField(max_length=64)
    destino = models.CharField(max_length=64)
    duracion = models.IntegerField()

    def __str__(self):
        return f"Vuelo #{self.id}: {self.origen} hacia {self.destino}"

# un_vuelo = Vuelo("Posadas","Buenos Aires", 2)
# un_vuelo.save()
# Vuelo.objects.all()
