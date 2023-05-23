from django.shortcuts import render
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.decorators import login_required
from Blogregistro.views import obtener_avatar

# Create your views here.

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario = request.user
            receptor = info['receptor']
            mensaje = info['mensaje']
            fecha = info['fecha']
            mensaje = Mensaje(usuario=usuario, receptor=receptor, mensaje=mensaje, fecha=fecha)
            mensaje.save()
            return render(request, 'Blogapp/inicio.html', {'mensaje': 'mensaje enviado correctamente', 'avatar': obtener_avatar(request)})
        else:
            return render(request, 'Blogapp/enviar_mensaje.html', {'form': form, 'mensaje': 'mensaje no enviado', 'avatar': obtener_avatar(request)})
    else:
        form = MensajeForm()
        return render(request, 'Blogapp/enviar_mensaje.html', {'form': form, 'avatar': obtener_avatar(request)})

@login_required
def mensajes(request):
    return render(request, 'Blogapp/mensajes.html', {'avatar': obtener_avatar(request)})

@login_required
def casilla_mensajes(request):
    if request.user.is_authenticated:
        mensajes = Mensaje.objects.filter(receptor=request.user)
        if len(mensajes) != 0:
            return render(request, 'Blogapp/casilla_mensajes.html', {'mensajes': mensajes, 'avatar': obtener_avatar(request)})
        else:
            return render(request, 'Blogapp/casilla_mensajes.html', {'mensaje': 'No hay mensajes', 'avatar': obtener_avatar(request)})

@login_required
def mostrar_mensaje(request, id):
    mensaje = Mensaje.objects.get(id=id)
    mensaje.leido = True
    mensaje.save()
    return render(request, 'Blogapp/mostrarMensaje.html', {'mensaje': mensaje, 'avatar': obtener_avatar(request)})

@login_required
def eliminar_mensaje(request, id):
    mensaje = Mensaje.objects.get(id=id)
    mensaje.delete()
    return render(request, 'Blogapp/inicio.html', {'mensaje': 'mensaje eliminado correctamente', 'avatar': obtener_avatar(request)})

@login_required
def responder_mensaje(request, id):
    mensaje = Mensaje.objects.get(id=id)
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario = request.user
            receptor = info['receptor']
            mensaje = info['mensaje']
            fecha = info['fecha']
            mensaje = Mensaje(usuario=usuario, receptor=receptor, mensaje=mensaje, fecha=fecha)
            mensaje.save()
            return render(request, 'Blogapp/inicio.html', {'mensaje': 'mensaje enviado correctamente', 'avatar': obtener_avatar(request)})
        else:
            return render(request, 'Blogapp/enviar_mensaje.html', {'form': form, 'mensaje': 'mensaje no enviado', 'avatar': obtener_avatar(request)})
    else:
        form = MensajeForm()
        return render(request, 'Blogapp/enviar_mensaje.html', {'form': form, 'mensaje': mensaje, 'avatar': obtener_avatar(request)})