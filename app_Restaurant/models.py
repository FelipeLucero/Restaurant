from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.


class Financiera(models.Model):
    id_financiera = models.IntegerField(primary_key=True)
    nombre_financiera = models.CharField(max_length=50)
    rut_financiera= models.CharField(max_length=12)
    
    def __str__(self):
        return self.rut_financiera

    class Meta:
        permissions = (
            ('financiera',_('Es financiera')),
        )


class Bodeguero(models.Model):
    id_bodeguero = models.IntegerField(primary_key=True)
    nombre_bodeguero = models.CharField(max_length=50)
    rut_bodeguero= models.CharField(max_length=12)
    
    def __str__(self):
        return self.rut_bodeguero

    class Meta:
        permissions = (
            ('bodeguero',_('Es bodeguero')),
        )



class Administrador(models.Model):
    id_administrador = models.IntegerField(primary_key=True)
    nombre_administrador = models.CharField(max_length=50)
    rut_administrador= models.CharField(max_length=12)
    
    def __str__(self):
        return self.rut_administrador

    class Meta:
        permissions = (
            ('administrador',_('Es administrador')),
        )


class Cocinero(models.Model):
    id_cocinero = models.IntegerField(primary_key=True)
    nombre_cocinero = models.CharField(max_length=50)
    rut_cocinero= models.CharField(max_length=12)
    
    def __str__(self):
        return self.rut_cocinero

    class Meta:
        permissions = (
            ('cocinero',_('Es cocinero')),
        )

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=50)
    rut_cliente= models.CharField(max_length=12)
    
    def __str__(self):
        return self.rut_cliente

    class Meta:
        permissions = (
            ('cliente',_('Es cliente')),
        )