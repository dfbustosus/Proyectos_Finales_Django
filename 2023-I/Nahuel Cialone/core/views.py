from django.shortcuts import render, redirect
from item.models import Categoria, Item
from .forms import Registro

def index(request):
    #traigo 6 items que estan disponibles "no vendidos" y las categorias disponibles
    items = Item.objects.filter(vendido=False)[0:6]
    categorias = Categoria.objects.all()
    #agregamos items y categorias al context para que pueda representarlos
    return render(request, 'core/index.html', {
        'categorias': categorias,
        'items':items,
    })

def contacto(request):
    return render(request, 'core/contacto.html')

def registro(request):
    if request.method == 'POST':
        formulario = Registro(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            
            return redirect('/login/')
    else:
        formulario = Registro()
    
    return render(request, 'core/registro.html',{
        'formulario': formulario
    })