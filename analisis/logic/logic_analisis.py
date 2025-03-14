from analisis.forms import AnalisisForm
from ..models import Analisis

def get_analisis():
    queryset = Analisis.objects.all()
    return (queryset)

def obtener_examen_eeg(form_data):
    """
    Función para obtener solo el atributo 'examen_eeg' del formulario AnalisisForm.
    
    :param form_data: Diccionario con los datos del formulario
    :return: Valor del campo 'examen_eeg' o None si no está presente
    """
    form = AnalisisForm(form_data)  # Crear una instancia del formulario con los datos
    if form.is_valid():  # Validar el formulario
        return form.cleaned_data.get('examen_eeg')  # Obtener solo el examen_eeg
    return None  # Retorna None si el formulario no es válido

def create_analisis(form):
    examen = form.cleaned_data.get('examen_eeg')  # Obtener el examen_eeg
    archivo = examen.archivo
    
    
    
    analisis = form.save()
    analisis.save()
    return ()

