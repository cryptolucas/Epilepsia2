from django.shortcuts import render


from analisis.forms import AnalisisForm
from analisis.logic.logic_analisis import create_analisis, get_analisis
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def analisis_list(request):
    analisis = get_analisis()
    context = {
        'analisis_list': analisis
    }
    return render(request, 'Analisis/analisis.html', context)

def analisis_create(request):
    if request.method == 'POST':
        form = AnalisisForm(request.POST)
        if form.is_valid():
            create_analisis(form)
            messages.add_message(request, messages.SUCCESS, 'Analisis create successful')
            return HttpResponseRedirect(reverse('AnalisisCreate'))
        else:
            print(form.errors)
    else:
        form = AnalisisForm()

    context = {
        'form': form,
    }

    return render(request, 'Analisis/analisisCreate.html', context)