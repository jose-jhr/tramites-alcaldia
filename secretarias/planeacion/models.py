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
 
class tramites_sec(models.Model):
    id_tramite_sec = models.AutoField(primary_key=True)
    id_tramite_tip = models.CharField(max_length=50)
    tip_tramites_tip = models.CharField(max_length=100)
    nombre_tramite_sec = models.CharField(max_length=200)
    nombre_solic = models.CharField(max_length=100)
    num_ide_solic = models.CharField(max_length=100)
    contacto_solic = models.CharField(max_length=100)
    correo_solic = models.CharField(max_length=100)
    fecha_solic = models.DateField()
    estado_solic = models.CharField(max_length=100)
    observacion_solic = models.CharField(max_length=100)
    #received file
    documento_solic = models.FileField()

    def __str__(self):
        tramites_sec = str(self.id_tramite_sec)+ " " + self.id_tramite_tip+ " " + self.tip_tramites_tip+ " " + self.nombre_tramite_sec+ " " + self.nombre_solic+ " " + self.num_ide_solic+ " " + self.contacto_solic+ " " + self.correo_solic+ " " + str(self.fecha_solic)+ " " + self.estado_solic+ " " + self.observacion_solic
        return tramites_sec


    
    
 