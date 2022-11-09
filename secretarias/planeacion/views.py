from django.shortcuts import render
from .models import tip_tramites

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
 
    
    

  