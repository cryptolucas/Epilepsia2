import os

import numpy as np
from analisis.forms import AnalisisForm
from ..models import Analisis
import mne
from django.conf import settings

def get_analisis():
    queryset = Analisis.objects.all()
    return (queryset)



def create_analisis(form):
    examen = form.cleaned_data.get('examen_eeg')  # Obtener el examen_eeg
    archivo = examen.archivo
    
    try:
        

        carpeta_edf = os.path.join(settings.BASE_DIR, "archivos_edf")
        archivo_path = os.path.join(carpeta_edf, archivo)

        if not os.path.exists(archivo_path):
            return {"error": "El archivo no existe en la ruta especificada."}

        # Cargar el archivo EDF con MNE
        raw = mne.io.read_raw_edf(archivo_path, preload=True)

        # Obtener los datos del EEG en un array de NumPy
        data, times = raw[:]

        # Detectar valores atípicos (picos altos)
        threshold = np.mean(data) + 3 * np.std(data)  # Umbral de anomalías (3 sigma)
        anomalous_points = np.where(abs(data) > threshold)

        # Crear lista de anomalías encontradas
        anomalias = []
        for ch_idx, time_idx in zip(*anomalous_points):
            canal = raw.ch_names[ch_idx]
            tiempo = times[time_idx]
            anomalias.append(f"Posible anomalía en canal {canal} en t={tiempo:.2f}s")

        # Resumen de detección
        resultado = {
            "nombre_archivo": archivo,
            "canales": raw.ch_names,
            "frecuencia_muestreo": raw.info["sfreq"],
            "duracion": raw.n_times / raw.info["sfreq"],
            "anomalias_detectadas": anomalias if anomalias else "No se detectaron anomalías significativas"
        }
        
        canales_str = ", ".join(resultado["canales"][0:2])
        
        descripcion = (
       
        f"- Duración: {resultado["duracion"]} segundos\n"
        f"- Canales analizados: {canales_str}\n"
        f"- Frecuencia muestreo: {resultado["frecuencia_muestreo"]}"
            )
        
        fecha = form.cleaned_data.get('fecha_analisis')
        anomalias_str = ", ".join(anomalias[0:3])
        analisis = Analisis.objects.create(examen_eeg = examen, descripcion = descripcion, 
                                           deteccion_anomalias = anomalias_str,
                                           fecha_analisis = fecha
                                           )
        analisis.save()
        return()

        # return resultado

    except Exception as e:
        return {"error": f"Ocurrió un error: {str(e)}"}
    
    # analisis = form.save()
    # analisis.save()
    # return ()

