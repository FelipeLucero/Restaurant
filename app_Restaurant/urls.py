
from django.urls import path
from . import views 
from .views import inicio, registro, RegistroUsuario, exito, login_exito, login_salida,testapi,IngresoEgresos, DatosClientesAdmin, InventarioAdministrador, ResumenAdmin, DatosMesasAdmin, platillos, reserva, MostrarMovimientos, MostrarProveedores, stock, MostrarSolicitudesProveedores, recetas, pedidos,MostrarMovimientosFinancieros,movimientos,pagaFinanciera,listarGanancias,listarGananciasMes, detalleBodega,soliRechazadaBodega,soliAprobadaBodega

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
    path('MenuCliente',login_required(login_exito) , name='MenuCLiente'),
    path('testapi',testapi , name='testapi'),

    path('IngresoEgresos',IngresoEgresos , name='IngresoEgresos'),
    path('financieraListarIngresosDias',listarGanancias , name='financieraListarIngresosDias'),
    path('financieraListarIngresosMes',listarGananciasMes , name='financieraListarIngresosMes'),

    path('Inventario',InventarioAdministrador, name='InventarioAdministrador'),
    path('DatosClientes',DatosClientesAdmin, name='DatosClientesAdmin'),
    path('Resumen',ResumenAdmin, name='ResumenAdmin'),
    path('DatosMesas',DatosMesasAdmin, name='DatosMesasAdmin'),

    path('MostrarMovimientos',MostrarMovimientos, name='MostrarMovimientos'),
    path('MostrarProveedores',MostrarProveedores, name='MostrarProveedores'),
    path('MostrarSolicitudesProveedores',MostrarSolicitudesProveedores, name='MostrarSolicitudesProveedores'),
    path('MostrarMovimientosFinancieros',MostrarMovimientosFinancieros, name='MostrarMovimientosFinancieros'),
    path('pagadosFinanciera',pagaFinanciera, name='pagadosFinanciera'),

    path('platillosCliente',platillos, name='platillosCliente'),
    path('reservaCliente',reserva, name='reservaCliente'),

    path('recetasCocinero',recetas, name='recetasCocinero'),
    path('pedidosCocinero',pedidos, name='pedidosCocineros'),

    path('stockBodeguero',stock, name='stockBodeguero'),
    path('movimientosBodega',movimientos, name='movimientosBodega'),
    path('detalleSolicitudesBodeguero',detalleBodega, name='detalleSolicitudesBodeguero'),
    path('solicitudRechazadaBodeguero',soliRechazadaBodega, name='solicitudRechazadaBodeguero'),
    path('solicitudAprobadaBodeguero',soliAprobadaBodega, name='solicitudAprobadaBodeguero'),

    path('logged_out',login_salida , name='logged_out'),
    url(r'registro', RegistroUsuario.as_view(), name="registro")
]




