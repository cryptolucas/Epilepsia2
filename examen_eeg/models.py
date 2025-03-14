from datetime import date
from django.db import models


from paciente.models import Paciente

# Create your models here.

# Create your models here.
class ExamenEEG(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    archivo = models.CharField(max_length=500)
    fecha_analisis = models.DateField(default=date.today)
    anotaciones = models.CharField(max_length=1000)
    

    def __str__(self):
         return f'Fecha: {self.fecha_analisis} - Cedula Paciente: {self.paciente.cedula}'
        