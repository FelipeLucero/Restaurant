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


def ListarEgresos(request):
    return render(request, 'plantillas/FinancieraListarEgresos.html')  # plantilla listado egresos

def AdminDatosClientes(request):
    return render(request, 'plantillas/AdminDatosClientes.html')

def AdminInventario(request):
    return render(request, 'plantillas/AdminInventario.html') 

def AdminAlertaBodega(request):
    return render(request, 'plantillas/AdminAlertaBodega.html')

def CalculoFinanciera(request):
    return render(request, 'plantillas/CalculoMovimientosFinanciera.html') 

def MostrarProveedores(request):
    return render(request, 'plantillas/Proveedores.html') 

 
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

# para Usuario Bodeguero.
def stock(request):
   return render(request, 'plantillas/stockBodeguero.html')   # plantilla de cliente para mostrar platillos.

# para Usuario Financiera.

# para Usuario Cocinero.