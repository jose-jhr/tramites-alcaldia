from django.db import models

# Create your models here.
class tip_tramites(models.Model):
    id_tramite = models.AutoField(primary_key=True)
    nombre_tramite = models.CharField(max_length=50)
    descripcion_tramite = models.CharField(max_length=100)
    responsable_tramite = models.CharField(max_length=200)

    def __str__(self):
        tip_tramites = str(self.id_tramite)+ " " + self.nombre_tramite+ " " + self.descripcion_tramite+ " " + self.responsable_tramite

        return tip_tramites
 
 