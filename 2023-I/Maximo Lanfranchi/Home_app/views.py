from django.shortcuts import render, get_object_or_404, redirect
from Usuario_app.models import Avatar
from django.contrib.auth.decorators import login_required
from .forms import MensajeForm
from .models import Mensaje, User

# Create your views here.
def home(request):
    return render(request, 'Home_app/inicio.html')



@login_required
def avatar(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    esta = Avatar.objects.filter(user=request.user.id).exists()
    if esta:
        return render(request, 'Home_app/inicio.html', {"url":avatares[0].imagen.url})
    else:
        return render(request, 'Home_app/inicio.html')



@login_required
def mensaje_lista(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    mensajes_enviados = Mensaje.objects.filter(remitente=request.user)
    return render(request, 'Home_app/mensaje_lista.html', {'mensajes_recibidos': mensajes_recibidos, 'mensajes_enviados': mensajes_enviados})

@login_required
def mensaje_conversacion(request, destinatario_id):
    destinatario = get_object_or_404(User, id=destinatario_id)
    mensajes_enviados_recibidos = Mensaje.objects.filter(destinatario=request.user, remitente=destinatario) | Mensaje.objects.filter(destinatario=destinatario, remitente=request.user)
    return render(request, 'Home_app/mensaje_conversacion.html', {'destinatario': destinatario, 'mensajes': mensajes_enviados_recibidos})

@login_required
def mensaje_nuevo(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('mensaje_lista')
    else:
        form = MensajeForm()
    return render(request, 'Home_app/mensaje_nuevo.html', {'form': form})


@login_required
def mensaje_eliminar(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, id=mensaje_id)
    if mensaje.remitente == request.user or mensaje.destinatario == request.user:
        mensaje.delete()
    return redirect('mensaje_lista')



