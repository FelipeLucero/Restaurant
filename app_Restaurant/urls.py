
from django.urls import path
from . import views 
from .views import inicio






urlpatterns = [
    path('', views.post_list, name='post_list '),
    path('Restaurant', inicio, name='Restaurant'),
]




