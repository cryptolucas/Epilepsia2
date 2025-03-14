from django import forms
from .models import Analisis

class AnalisisForm(forms.ModelForm):
    class Meta:
        model = Analisis
        fields = [
            'examen_eeg',
            # 'descripcion',
            # 'deteccion_anomalias',
            'fecha_analisis'
        ]

        labels = {
            'examen_eeg': 'Examen_eeg',
            # 'descripcion': 'Descripcion',
            # 'deteccion_anomalias': 'Deteccion_anomalias',
            'fecha_analisis': 'Fecha_analisis'
            
        }