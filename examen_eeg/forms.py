from django import forms
from .models import ExamenEEG

class ExamenEEGForm(forms.ModelForm):
    class Meta:
        model = ExamenEEG
        fields = [
            'paciente',
            'archivo',
            'fecha_analisis',
            'anotaciones'
        ]

        labels = {
            'paciente' : 'Paciente',
            'archivo': 'Archivo',
            'fecha_analisis': 'Fecha_analisis',
            'anotaciones': 'Anotaciones'
        }
        
    archivo = forms.FileField(required=True)  # Campo de archivo obligatorio