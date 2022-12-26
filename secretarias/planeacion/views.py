from django.shortcuts import render
from .models import tip_tramites
from .models import tramites_sec

# Create your views here.
def home(request):
    return render(request, 'menu.html')

def ges_tip_tramites(request):
    return render(request, 'gestion_tip_tramites.html')

def menu(request):
    return render(request, 'menu.html')

def register_tip_tramite(request):
    nombre_tramite = request.POST['nombre_tramite']
    responsable_tramite = request.POST['responsable_tramite']
    descripcion_tramite = request.POST['descripcion_tramite']
    #show nombre_tramite
    tip_tramites_obj = tip_tramites(nombre_tramite=nombre_tramite,
     responsable_tramite=responsable_tramite, descripcion_tramite=descripcion_tramite)
    tip_tramites_obj.save()
    return render(request, 'menu.html')
 
    
def agregar_tramite(request):
    tipo_tramites = tip_tramites.objects.all()
    #print for console
    print(tipo_tramites)
    return render(request, 'agregar_tramite.html', {'tipo_tramites': tipo_tramites})

def register_tramite(request):
    id_tramite_tip = request.POST['id_tramite_tip']
    tip_tramites_tip = request.POST['tip_tramites_tip']
    nombre_tramite_sec = request.POST['nombre_tramite_sec']
    nombre_solic = request.POST['nombre_solic']
    num_ide_solic  = request.POST['num_ide_solic']
    contacto_solic = request.POST['contacto_solic']
    correo_solic = request.POST['correo_solic']
    fecha_solic = request.POST['fecha_solic']
    state_solicitud = request.POST['state_solicitud']
    observacion = request.POST['observaciones']
    formFile = request.FILES['formFile']
    
    tramites_sec_obj = tramites_sec(id_tramite_tip=id_tramite_tip,tip_tramites_tip=tip_tramites_tip,nombre_tramite_sec=nombre_tramite_sec,nombre_solic=nombre_solic,num_ide_solic=num_ide_solic,contacto_solic=contacto_solic,correo_solic=correo_solic,fecha_solic=fecha_solic,estado_solic=state_solicitud,observacion_solic=observacion,documento_solic=formFile)
    tramites_sec_obj.save()





    return render(request, 'menu.html')
    

  