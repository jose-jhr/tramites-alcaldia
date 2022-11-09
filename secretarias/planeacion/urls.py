from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gestion_tip_tramites', views.ges_tip_tramites, name='ges_tip_tramites'),
    path('menu',views.menu, name='menu'),
    path('register_tip_tramite', views.register_tip_tramite, name='register_tip_tramite')
]