from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

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

User = get_user_model()  # Obtén el modelo de usuario existente

# Modelo de Roles
class Role(models.Model):
    nombre_rol = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    fecha_eliminacion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])

    def __str__(self):
        return self.nombre_rol

# models.py
class UsuarioRoles(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Role, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_now_add=True)
    fecha_revocacion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('revocado', 'Revocado')])

    def __str__(self):
        return f"{self.usuario.username} - {self.rol.nombre_rol}"
    
User = get_user_model()

class Logbook(models.Model):
    bitacora = models.TextField()  # Cambiado a TextField para almacenar textos largos
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)  # Evita la eliminación de usuarios si hay bitácoras asociadas
    datacenter = models.ForeignKey('Datacenter', on_delete=models.PROTECT)  # Evita la eliminación de datacenters si hay bitácoras asociadas
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Guarda fecha y hora de creación

    def __str__(self):
        return f"Bitácora de {self.usuario.username} - {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
    
    