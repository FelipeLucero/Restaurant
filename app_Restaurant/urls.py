
from django.urls import path
from . import views 
from .views import inicio, registro, RegistroUsuario, exito, login_exito, login_salida,testapi,IngresoEgresos, DatosClientesAdmin,ReservasClienteAdmin,PedidosAdmin,PedidoTerminadoAdmin,SolicitudListaAdmin,SolicitudAdmin,ProveedorActivoAdmin,ProveedorInactivoAdmin,PedidosPendienteAdmin,PedidosAnuladosAdmin,EstadoFacturaAdmin,SolicitudProveedorAdmin, InventarioAdministrador, ResumenAdmin,estadoBodegaAdmin, DatosMesasAdmin, platillos, reserva, MostrarMovimientos, MostrarProveedores, stock, MostrarSolicitudesProveedores, recetas, pedidos,MostrarMovimientosFinancieros,movimientos,pagaFinanciera,listarGanancias,listarGananciasMes, detalleBodega,platillos,platillosListos,CambiarEstadoFactura,MostarFacturasPagadas

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

    path('IngresoEgresos',login_required(IngresoEgresos) , name='IngresoEgresos'),
    path('financieraListarIngresosDias',login_required(listarGanancias) , name='financieraListarIngresosDias'),
    path('financieraListarIngresosMes',login_required(listarGananciasMes) , name='financieraListarIngresosMes'),
    path('CambiarEstadoFactura',login_required(CambiarEstadoFactura) , name='CambiarEstadoFactura'),

    path('Inventario',login_required(InventarioAdministrador), name='InventarioAdministrador'),
    path('DatosClientes',login_required(DatosClientesAdmin), name='DatosClientesAdmin'),
    path('Resumen',login_required(ResumenAdmin), name='ResumenAdmin'),
    path('DatosMesas',login_required(DatosMesasAdmin), name='DatosMesasAdmin'),
    path('EstadoBodega',login_required(estadoBodegaAdmin), name='estadoBodegaAdmin'),
    path('SolicitudProv',login_required(SolicitudProveedorAdmin), name='SolicitudProveedorAdmin'),
    path('ReservaCliente',login_required(ReservasClienteAdmin), name='ReservasClienteAdmin'),
    path('SolicitudLista',login_required(SolicitudListaAdmin), name='SolicitudListaAdmin'),
    path('Pedidos',login_required(PedidosAdmin), name='PedidosAdmin'),
    path('PedidosPendientes',login_required(PedidosPendienteAdmin), name='PedidosPendienteAdmin.html'),
    path('PedidoTerminado',login_required(PedidoTerminadoAdmin), name='PedidoTerminadoAdmin'),
    path('PedidosAnulados',login_required(PedidosAnuladosAdmin), name='PedidosAnuladosAdmin'),
    path('EstadoFactura',login_required(EstadoFacturaAdmin), name='EstadoFacturaAdmin'),
    path('ProveedorActivo',login_required(ProveedorActivoAdmin), name='ProveedorActivoAdmin'),
    path('ProveedorInactivo',login_required(ProveedorInactivoAdmin), name='ProveedorInactivoAdmin'),
    path('Solicitud',login_required(SolicitudAdmin), name='SolicitudAdmin'),

    path('MostrarMovimientos',login_required(MostrarMovimientos), name='MostrarMovimientos'),
    path('MostrarProveedores',login_required(MostrarProveedores), name='MostrarProveedores'),
    path('MostrarSolicitudesProveedores',login_required(MostrarSolicitudesProveedores), name='MostrarSolicitudesProveedores'),
    path('MostrarMovimientosFinancieros',login_required(MostrarMovimientosFinancieros), name='MostrarMovimientosFinancieros'),
    path('pagadosFinanciera',login_required(pagaFinanciera), name='pagadosFinanciera'),
    path('MostarFacturasPagadas',login_required(MostarFacturasPagadas), name='MostarFacturasPagadas'),

    path('platillosCliente',login_required(platillos), name='platillosCliente'),
    path('reservaCliente',login_required(reserva), name='reservaCliente'),

    path('recetasCocinero',login_required(recetas), name='recetasCocinero'),
    path('pedidosCocinero',login_required(pedidos), name='pedidosCocineros'),
    path('platillosListosCocinero',login_required(platillosListos), name='platillosListosCocinero'),

    path('stockBodeguero',login_required(stock), name='stockBodeguero'),
    path('movimientosBodega',login_required(movimientos), name='movimientosBodega'),
    path('detalleSolicitudesBodeguero',login_required(detalleBodega), name='detalleSolicitudesBodeguero'),
 

    path('logged_out',login_salida , name='logged_out'),
    url(r'registro', RegistroUsuario.as_view(), name="registro")
]




