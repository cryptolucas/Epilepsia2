from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('analisis/', views.analisis_list),
    path('analisisCreate/', csrf_exempt(views.analisis_create), name='AnalisisCreate'),
]