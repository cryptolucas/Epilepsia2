from django.shortcuts import render

from paciente.forms import PacienteForm
from paciente.logic.logic_paciente import create_paciente, get_pacientes

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from epilepsia2.auth0backend import getRole

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