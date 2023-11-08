from django.db import models

class Auto(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    numero_de_ruedas = models.IntegerField()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"
