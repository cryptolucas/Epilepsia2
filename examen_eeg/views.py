from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from google.cloud import storage
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from examen_eeg.logic.logic_examen_eeg import create_examenEEG
from examen_eeg.forms import ExamenEEGForm

BUCKET_NAME = "epilepsia2-bucket"  # Nombre del bucket en GCP

def upload_to_gcp(file):
    """Sube un archivo a Cloud Storage y retorna la URL pública."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob({file.name})

    blob.upload_from_file(file, content_type=file.content_type)
    blob.make_public()  # Hace que el archivo sea accesible públicamente

    return blob.public_url

def examenEEG_create(request):
    if request.method == 'POST':
        form = ExamenEEGForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            public_url = upload_to_gcp(archivo)  # Subir archivo a GCP y obtener URL

            examen = form.save(commit=False)
            examen.archivo = public_url  # Guardar la URL del archivo en el modelo
            examen.save()

            messages.success(request, 'Examen EEG creado exitosamente')
            return HttpResponseRedirect(reverse('ExamenEEGCreate'))
        else:
            print(form.errors)
    else:
        form = ExamenEEGForm()

    return render(request, 'ExamenEEG/examenEEGCreate.html', {'form': form})
