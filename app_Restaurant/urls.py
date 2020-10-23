
from django.urls import path
from . import views 
from .views import inicio, registro, RegistroUsuario, exito, login_exito, login_salida,testapi,IngresoEgresos,ListarEgresos,AdminDatosClientes,AdminInventario,AdminAlertaBodega

from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.post_list, name='post_list '),
    path('Restaurant', inicio, name='Restaurant'),
    path('RegistroExitoso', exito, name='exito'),
     
    path('MenuBodeguero',login_required(login_exito) , name='MenuBodeguero'),
    path('MenuCocinero',login_required(login_exito) , name='MenuCocinero'),
    path('MenuFinanciera',login_required(login_exito) , name='MenuFinanciera'),
    path('MenuAdministrador',login_required(login_exito) , name='MenuAdministrador'),
    path('reserva',login_required(login_exito) , name='reserva'),
    path('testapi',testapi , name='testapi'),
    path('IngresoEgresos',IngresoEgresos , name='IngresoEgresos'),
    path('ListarEgresos',ListarEgresos , name='ListarEgresos'),
    path('Inventario',AdminInventario, name='AdminInventario'),
    path('DatosClientes',AdminDatosClientes, name='AdminDatosClientes'),
    path('AlertaBodega',AdminAlertaBodega, name='AdminAlertaBodega'),

    path('logged_out',login_salida , name='logged_out'),
    url(r'registro', RegistroUsuario.as_view(), name="registro")
]




