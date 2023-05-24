from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .models import Conversacion
from .forms import MensajeForm

@login_required
def nueva_conversacion(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.creador == request.user:
        return redirect('dashboard:index')
    
    #chequeamos si el id pertenece a alguno de los miembros y podemos proceder
    conversaciones = Conversacion.objects.filter(item=item).filter(miembros__in=[request.user.id])
    
    if conversaciones:
        return redirect('mensajes:detalle', pk=conversaciones.first().id)
    
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        
        if form.is_valid():
            conversacion = Conversacion.objects.create(item=item)
            conversacion.miembros.add(request.user)
            conversacion.miembros.add(item.creador)
            conversacion.save()
            
            mensaje_conversacion = form.save(commit=False)
            mensaje_conversacion.conversacion = conversacion
            mensaje_conversacion.creador = request.user
            mensaje_conversacion.save()
            
            return redirect('item:detalle', pk=item_pk)
    else:
        form = MensajeForm()
    
    return render(request, 'mensajes/nuevo.html',{
        'form': form
    })

@login_required
def inbox(request):
    conversaciones = Conversacion.objects.filter(miembros__in=[request.user.id])
    
    return render(request, 'mensajes/inbox.html', {
        'conversaciones': conversaciones
    })

@login_required
def detalle(request, pk):
    conversacion = Conversacion.objects.filter(miembros__in=[request.user.id]).get(pk=pk)
    
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        
        if form.is_valid():
            mensaje_conversacion = form.save(commit=False)
            mensaje_conversacion.conversacion = conversacion
            mensaje_conversacion.creador = request.user
            mensaje_conversacion.save()
            
            conversacion.save()
            
            return redirect('mensajes:detalle', pk=pk)
    else:
        form = MensajeForm()
    
    return render(request, 'mensajes/detalle.html',{
        'conversacion': conversacion,
        'form': form,
    })