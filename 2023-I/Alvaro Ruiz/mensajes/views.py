from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensajeria
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CrearMensajeForm
from django.contrib.auth import models
from django.contrib.auth.models import User

# Create your views here.

def progreso(request):
    return HttpResponse('MENSAJES EN PROGRESO...')

@login_required
def lista_conversaciones(request):
    conversaciones = Mensajeria.objects.filter(remitente=request.user) | Mensajeria.objects.filter(destinatario = request.user)
    conversaciones.distinct('remitente', 'destinatario')

    return render(request, 'lista_conversaciones.html', {
        'conversaciones': conversaciones,
    })

@login_required
def detalle_conversaciones(request, destinatario_id):
    print(destinatario_id)
    conversacion_remitente = Mensajeria.objects.filter(remitente = request.user, destinatario_id = destinatario_id)
    conversacion_destinatario = Mensajeria.objects.filter(remitente= destinatario_id, destinatario = request.user)
    conversacion = conversacion_remitente.union(conversacion_destinatario).order_by('horaDeEnvio')

    form = CrearMensajeForm()
    dest_id = destinatario_id
    return render(request, 'detalle_conversaciones.html', {
        'conversacion': conversacion,
        'form':form,
        'dest_id':dest_id
        })

@login_required
def enviar_mensajes(request, destinatario_id):
    destinatario = get_object_or_404(User, id=destinatario_id)
    if request.method == 'POST':
        form = CrearMensajeForm(request.POST)
        print(form)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente_id = request.user
            mensaje.destinatario_id = destinatario
            mensaje.save()

            return redirect('detalle_conversaciones', {"destinatario_id": destinatario_id})
        else:
            form = CrearMensajeForm()
        return render(request, 'enviar_mensaje.html', {'form':form, 'destinatario': destinatario_id})