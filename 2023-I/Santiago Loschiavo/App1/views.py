from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'App1/inicio.html')

def productos(request):
    return render(request, 'App1/productos.html')

def servicios(request):
    return render(request, "App1/servicios.html")

def sobre_mi(request):
    return render(request, 'App1/sobre_mi.html')

def contacto(request):
    return render(request, 'App1/contacto.html')
