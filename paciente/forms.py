from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'tipo_sangre',
            'rh',
            'cedula',
            'alergias',
            'eps',
            'telefono'
            
        ]

        labels = {
            
            'nombre' : 'Nombre',
            'tipo_sangre': 'Tipo_sangre',
            'rh': 'Rh',
            'cedula': 'Cedula',
            'alergias': 'Alergias',
            'eps': 'Eps',
            'telefono': 'Telefono'
            
        }