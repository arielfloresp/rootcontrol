from django.db import models

# Create your models here.

from django.db import models

class Datacenter(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('eliminado', 'Eliminado')
    ]

    id = models.AutoField(primary_key=True)
    codigo = models.CharField(null=False, max_length=255)
    propietario = models.CharField( max_length=100)
    nombre = models.CharField(null=False, max_length=100)
    ubicacion = models.CharField(null=False, max_length=255)
    nota = models.CharField(max_length=255)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    fecha_eliminacion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return self.nombre
