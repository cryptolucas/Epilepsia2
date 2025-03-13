from datetime import date
from django.db import models

from examen_eeg.models import ExamenEEG


# Create your models here.
class Analisis(models.Model):
    
    examen_eeg = models.OneToOneField(ExamenEEG, on_delete=models.CASCADE, primary_key=True)
    descripcion = models.CharField(max_length=1000)
    deteccion_anomalias = models.CharField(max_length=1000, default=None)
    fecha_analisis = models.DateField(default=date.today)
    

    def __str__(self):
        return f'Análisis: {self.descripcion}  - Fecha: {self.fecha_analisis}'