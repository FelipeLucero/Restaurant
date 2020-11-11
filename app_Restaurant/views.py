from django.shortcuts import render

from django.views.generic import CreateView
from django.contrib.auth.models import User
from app_Restaurant.forms import RegistroForm
from django.urls import reverse_lazy


def post_list(request):
    return render(request, 'plantillas/Restaurant.html', {}) # plantilla determinada arranque.

def inicio(request):
    return render(request, 'plantillas/Restaurant.html')   # plantilla de inicio.

def registro(request):
   return render(request, 'plantillas/registro.html')   # plantilla registro de usuario.


def testapi(request):
    return render(request, 'plantillas/testapi.html')  # plantilla testeo conexion api

def IngresoEgresos(request):
    return render(request, 'plantillas/FinancieraIngresoEgresos.html')  # plantilla ingreso egresos





def MostrarMovimientos(request):
    return render(request, 'plantillas/MovimientosFinanciera.html') 

def MostrarProveedores(request):
    return render(request, 'plantillas/Proveedores.html') 

def MostrarSolicitudesProveedores(request):
    return render(request, 'plantillas/SolicitudesProveedoresFinanciera.html') 

def MostrarMovimientosFinancieros(request):
    return render(request, 'plantillas/MovimientosFinancierosFinanciera.html') 

def CambiarEstadoFactura(request):
    return render(request, 'plantillas/financieraCambiarEstadoFactura.html') 

def MostarFacturasPagadas(request):
    return render(request, 'plantillas/finacieraFacturasPagadas.html') 

 # para registrar usuario.
class RegistroUsuario(CreateView): 
    model = User
    template_name = "plantillas/registro.html"         
    form_class = RegistroForm
    success_url = reverse_lazy('exito')

# funcion para retornar registro_exitoso.
def exito(request):  
    return render(request, 'registration/RegistroExitoso.html')     

def login_exito(request):
    user = request.user

    if user.has_perm('app_Restaurant.financiera'):
        
        return render(request, 'plantillas/MenuFinanciera.html')   # plantilla con funciones para tecnico.

    if user.has_perm('app_Restaurant.bodeguero'):
        return render(request, 'plantillas/MenuBodeguero.html')   # plantilla con funciones para tecnico.

    if user.has_perm('app_Restaurant.cocinero'):
        return render(request, 'plantillas/MenuCocinero.html')   # plantilla con funciones para tecnico.

    if user.has_perm('app_Restaurant.administrador'):
        return render(request, 'plantillas/MenuAdministrador.html')   # plantilla con funciones para tecnico.

    else:
        
        return render(request, 'plantillas/MenuCliente.html')  # plantilla con funciones para cliente.   

    
def login_salida(request):
    return render(request, 'registration/logged_out.html')  # funcion para retornar logout.

# para Usuario Cliente.

def platillos(request):
   return render(request, 'plantillas/platillosCliente.html')   # plantilla de cliente para mostrar platillos.

def reserva(request):
   return render(request, 'plantillas/reservaCliente.html')   # plantilla de cliente para mostrar platillos.



# para Usuario Administrador.
def DatosClientesAdmin(request):
    return render(request, 'plantillas/DatosClientesAdmin.html')

def InventarioAdministrador(request):
    return render(request, 'plantillas/InventarioAdministrador.html') 

def ResumenAdmin(request):
    return render(request, 'plantillas/ResumenAdmin.html')

def DatosMesasAdmin(request):
    return render(request, 'plantillas/DatosMesasAdmin.html')

def estadoBodegaAdmin(request):
    return render(request, 'plantillas/estadoBodegaAdmin.html')

def SolicitudProveedorAdmin(request):
    return render(request, 'plantillas/SolicitudProveedorAdmin.html')

def ReservasClienteAdmin(request):
    return render(request, 'plantillas/ReservasClienteAdmin.html')

def ReservaFinalizadaAdmin(request):
    return render(request, 'plantillas/ReservaFinalizadaAdmin.html')

def SolicitudListaAdmin(reques):
    return render(reques, 'plantillas/SolicitudListaAdmin.html')

def PedidosPendienteAdmin(reques):
    return render(reques, 'plantillas/PedidosPendienteAdmin.html')

def PedidosAnuladosAdmin(reques):
    return render(reques, 'plantillas/PedidosAnuladosAdmin.html')

def GananciaDiaAdmin(reques):
    return render(reques, 'plantillas/GananciaDiaAdmin.html')

def ProveedorActivoAdmin(reques):
    return render(reques, 'plantillas/ProveedorActivoAdmin.html')

def ProveedorInactivoAdmin(reques):
    return render(reques, 'plantillas/ProveedorInactivoAdmin.html')

def ProductosAdmin(reques):
    return render(reques, 'plantillas/ProductosAdmin.html')

def SolicitudAdmin(reques):
    return render(reques, 'plantillas/SolicitudAdmin.html')

def PedidoTerminadoAdmin(reques):
    return render(reques, 'plantillas/PedidoTerminadoAdmin.html')

def PedidosAdmin(reques):
    return render(reques, 'plantillas/PedidosAdmin.html')

def PedidosPagadosAdmin(reques):
    return render(reques, 'plantillas/PedidosPagadosAdmin.html')

def PlatosAdmin(reques):
    return render(reques, 'plantillas/PlatosAdmin.html')

def GananciaMensualAdmin(reques):
    return render(reques, 'plantillas/GananciaMensualAdmin.html')

# para Usuario Bodeguero.
def stock(request):
   return render(request, 'plantillas/stockBodeguero.html')   # plantilla de cliente para mostrar platillos.

def movimientos(request):
   return render(request, 'plantillas/movimientosBodega.html')   # plantilla de cliente para mostrar platillos.


def detalleBodega(request):
   return render(request, 'plantillas/detalleSolicitudesBodeguero.html')   # plantilla de cliente para mostrar platillos.


def SolicitarInsumosBodega(request):
   return render(request, 'plantillas/solicitarInsumosBodeguero.html')   # plantilla de cliente para mostrar platillos.

# para Usuario Financiera.

def pagaFinanciera(request):
   return render(request, 'plantillas/pagadosFinanciera.html')   # plantilla de cliente para mostrar platillos.

def listarGanancias(request):
    return render(request, 'plantillas/financieraListarIngresosDias.html')  # plantilla listado egresos


def listarGananciasMes(request):
    return render(request, 'plantillas/financieraListarIngresosMes.html')  # plantilla listado egresos





# para Usuario Cocinero.

def recetas(request):
   return render(request, 'plantillas/recetasCocinero.html')   # plantilla de cliente para mostrar platillos.

def pedidos(request):
   return render(request, 'plantillas/pedidosCocinero.html')   # plantilla de cliente para mostrar platillos.


def platillosListos(request):
   return render(request, 'plantillas/PlatillosListosCocinero.html')   # plantilla de cliente para mostrar platillos.
