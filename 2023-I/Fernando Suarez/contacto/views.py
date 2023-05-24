from django.shortcuts import render, redirect
from .forms import formularioContacto

from django.core.mail import EmailMessage


def contacto(request):
    formulario_Contacto = formularioContacto( )

    if request.method =="POST":
        formulario_Contacto = formularioContacto( data= request.POST)

        if formulario_Contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje de App"
            "El usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {}".format(nombre, email, contenido),
            "", ["tetsukaikari3@gmail.com"], reply_to=[email])

            try:
                email.send()
                
                return redirect ("/contacto/?valido")
            
            except:
                return redirect ("/contacto/?invalido")


    return render(request, 'contacto/contacto.html', {'miFormulario': formulario_Contacto})

