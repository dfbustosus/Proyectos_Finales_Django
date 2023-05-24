from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from carrito.carrito import Carrito

from pedidos.models import LineaPedido, Pedido

from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.core.mail import send_mail

from .models import Producto


# Create your views here.


@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user) 
    carro=Carrito(request)  
    lineas_pedido=list()  
    for key, value in Carrito.carrito.items(): 
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido                 
            ))

    LineaPedido.objects.bulk_create(lineas_pedido) 
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
        

    )
    messages.success(request, "El pedido se ha creado correctamente")
    
    return redirect('../tienda')
   

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario")                        
        })

    mensaje_texto=strip_tags(mensaje)
    from_email="fernandosuarez1985@gmail.com"

    to="aquí la dirección del destinatario"
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)
    
