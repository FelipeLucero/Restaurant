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
        
        return render(request, 'plantillas/reserva.html')  # plantilla con funciones para cliente.   