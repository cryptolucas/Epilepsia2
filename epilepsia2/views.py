from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def healthCheck(request):
    print(dir(request))
    return HttpResponse('ok')