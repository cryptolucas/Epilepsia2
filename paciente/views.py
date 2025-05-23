from django.shortcuts import render

from paciente.forms import PacienteForm
from paciente.logic.logic_paciente import create_paciente, get_pacientes, get_paciente_por_cedula

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from epilepsia2.auth0backend import getRole
from django.contrib.auth.decorators import login_required

@login_required
def pacientes_list(request):
    role = getRole(request)
    if role == "medico" or role == "tecnico" or role == "enfermero":
        pacientes = get_pacientes()
        context = {
            'pacientes_list': pacientes
        }
        return render(request, 'Paciente/pacientes.html', context)
    else:
        return HttpResponse("Unauthorized User")
    
@login_required
def paciente_unico(request, cedula):
    paciente = get_paciente_por_cedula(cedula)
    context = {
            'pacientes_list': [paciente]
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