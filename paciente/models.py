from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=500)
    tipo_sangre = models.CharField(max_length=500)
    rh = models.CharField(max_length=500)
    cedula = models.CharField(max_length=500)
    alergias = models.CharField(max_length=500)
    eps = models.CharField(max_length=500)
    telefono = models.CharField(max_length=500)
    
    

    def __str__(self):
         return f'Nombre: {self.nombre} - Cédula: {self.cedula} - EPS: {self.eps}'