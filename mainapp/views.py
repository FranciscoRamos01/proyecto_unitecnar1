
from django.http import HttpResponse
from django.shortcuts import render

def pruebas(request):
    return HttpResponse("<h1>Bienvenido a Django desde Unitecnar</h1>")

def template_view(request):
    return render(request, 'index.html')
