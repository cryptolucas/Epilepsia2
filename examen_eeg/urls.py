from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('examenesEEG/', views.examenes_list),
    path('examenEEGcreate/', csrf_exempt(views.examenEEG_create), name='ExamenEEGCreate'),
]