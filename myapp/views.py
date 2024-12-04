from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from .utils import generar_graficas

# Create your views here.

def home(request):
 return render(request, "home.html")

def mostrar_graficas(request):
    graficas = generar_graficas()
    return render(request, 'graficas.html', {'graficas': graficas})
