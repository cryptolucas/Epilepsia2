from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('pacientes/', views.pacientes_list),
    path('pacientecreate/', csrf_exempt(views.pacientes_create), name='pacienteCreate'),
    path('paciente/<str:cedula>', views.paciente_unico, name='paciente_unico'),
]


