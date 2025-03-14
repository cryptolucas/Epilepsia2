from django.shortcuts import render

from examen_eeg.logic.logic_examen_eeg import get_examenesEEG, create_examenEEG
from examen_eeg.forms import ExamenEEGForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def examenes_list(request):
    examenes = get_examenesEEG()
    context = {
        'examenes_list': examenes
    }
    return render(request, 'ExamenEEG/examenesEEG.html', context)

def examenEEG_create(request):
    if request.method == 'POST':
        form = ExamenEEGForm(request.POST)
        if form.is_valid():
            create_examenEEG(form)
            messages.add_message(request, messages.SUCCESS, 'ExamenEEG create successful')
            return HttpResponseRedirect(reverse('ExamenEEGCreate'))
        else:
            print(form.errors)
    else:
        form = ExamenEEGForm()

    context = {
        'form': form,
    }

    return render(request, 'ExamenEEG/examenEEGCreate.html', context)