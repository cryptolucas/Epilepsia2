from django.shortcuts import render

from paciente.forms import PacienteForm
from paciente.logic.logic_paciente import create_paciente, get_pacientes

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def pacientes_list(request):
    pacientes = get_pacientes()
    context = {
        'pacientes_list': pacientes
    }
    return render(request, 'Paciente/pacientes.html', context)

def pacientes_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            create_paciente(form)
            messages.add_message(request, messages.SUCCESS, 'Paciente create successful')
            return HttpResponseRedirect(reverse('pacienteCreate'))
        else:
            print(form.errors)
    else:
        form = PacienteForm()

    context = {
        'form': form,
    }

    return render(request, 'Paciente/pacienteCreate.html', context)