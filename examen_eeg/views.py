from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from google.cloud import storage
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from examen_eeg.logic.logic_examen_eeg import create_examenEEG, get_examenesEEG
from examen_eeg.forms import ExamenEEGForm

BUCKET_NAME = "epilepsia2-bucket"  # Nombre del bucket en GCP


def examenes_list(request):
    examenes = get_examenesEEG()
    context = {
        'examenes_list': examenes
    }
    return render(request, 'ExamenEEG/examenesEEG.html', context)


def upload_to_gcp(file):
    """Sube un archivo a Cloud Storage y retorna la URL pública."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file.name)

    blob.upload_from_file(file, content_type=file.content_type)
    blob.make_public()  # Hace que el archivo sea accesible públicamente

    return blob.public_url

def examenEEG_create(request):
    if request.method == 'POST':
        form = ExamenEEGForm(request.POST, request.FILES)  # Se debe incluir request.FILES
        if form.is_valid():
            archivo = request.FILES.get('archivo')  # Obtener el archivo subido
            if archivo:
                public_url = upload_to_gcp(archivo)  # Subir a GCP y obtener la URL
                
                examen = form.save(commit=False)
                examen.archivo = public_url  # Guardar la URL en la base de datos
                examen.save()

                messages.success(request, 'Examen EEG creado exitosamente')
                return HttpResponseRedirect(reverse('ExamenEEGCreate'))
            else:
                messages.error(request, "No se ha subido ningún archivo.")
        else:
            print(form.errors)
    else:
        form = ExamenEEGForm()

    return render(request, 'ExamenEEG/examenEEGCreate.html', {'form': form})
