from django.contrib import admin
from django.urls import path
from web.views.listadmin import listView
from web.views.listadmin import listinternadoView
from web.views.listadmin import clienteView
from web.views.listadmin import MascotaView
from web.views.listadmin import vacunaView

from web.views.registroadmin import registroView
from web.views.registroadmin import registroclienteView
from web.views.registroadmin import registromascotaView
from web.views.registroadmin import registrovacunaView
from web.views.registroadmin import registrointernadoView
from web.views.admi import adminView
from web.views.web import hometView

from web.views.user import userhomeView
from web.views.user import userinternadoView
from web.views.user import usermascotaView
from web.views.user import usermascotahistoriaView
from web.views.user import usertarjetaView

urlpatterns = [
 
    path('lista', listView.as_view()),
    path('listainternado', listinternadoView.as_view()),
    path('listacliente', clienteView.as_view()),
    path('listamnascota', MascotaView.as_view()),
    path('listavacuna', vacunaView.as_view()),
    path('registro', registroView.as_view()),
    path('registrocliente', registroclienteView.as_view()),
    path('registromascota', registromascotaView.as_view()),
    path('registrovacuna', registrovacunaView.as_view()),
    path('registrointernado', registrointernadoView.as_view()),
    path('tablero', adminView.as_view()),
    path('home', hometView.as_view()),
    path('user', userhomeView.as_view()),
    path('userinternado', userinternadoView.as_view()),
    path('usermascota', usermascotaView.as_view()),
    path('userhistoria', usermascotahistoriaView.as_view()),
    path('usertarjeta', usertarjetaView.as_view()),

]