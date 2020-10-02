


from django.shortcuts import render




def post_list(request):
    return render(request, 'plantillas/Restaurant.html', {}) # plantilla determinada arranque.



def inicio(request):
    return render(request, 'plantillas/Restaurant.html')   # plantilla de inicio.

