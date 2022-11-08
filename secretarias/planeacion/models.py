from django.db import models

# Create your models here.
class tip_tramites(models.Model):
    id_tramite = models.CharField(max_length=10, primary_key=True)
    nombre_tramite = models.CharField(max_length=50)
    descripcion_tramite = models.CharField(max_length=100)
    responsable_tramite = models.CharField(max_length=200)
