from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login,logout,authenticate
from App1.forms import UserRegisterForm, UserEditForm , UserEditForm2 ,UserEditForm3 , AvatarFormulario
from django.contrib.auth.decorators import login_required
from App1.models import Avatar,Calificacion,Descripcion,Contacto
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings
from django.core.mail import send_mail


def inicio(request):
    return render(request,'App1/inicio.html')

"""def contactos(request):
    return render(request,'App1/contacto.html',)"""

def sugerencias(request):
    return render(request,'App1/sugerencias.html')

def calificacion(request):
    return render(request,'App1/calificacion.html') 

def getCalificaciones(request):
    calificacion = request.GET.get('calificacion')
    puntos = calificacion.objects.filter(calificacion__icontains=calificacion)
    return render(request, 'App1/getcalificacion.html', {'puntos': puntos}) 
    
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "App1/inicio.html", {"mensaje":f"Bienvenido {usuario}"}) and redirect('/')
            else:
                return render(request, "App1/login.html", {"mensaje":"Datos incorrectos"}) 
        else:
            return render(request, "App1/login.html", {"mensaje":"Formulario erroneo"}) 
    form = AuthenticationForm()
    return render(request, "App1/login.html", {"form": form})

def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  email = form.cleaned_data['email']

                  if User.objects.filter(username=username).exists():
                        return render(request, "App1/registro.html", {"mensaje": "ERROR", "form": form, "error_msg": "El nombre de usuario ya está en uso"})

            
                  if User.objects.filter(email=email).exists():
                        return render(request, "App1/registro.html", {"mensaje": "ERROR", "form": form, "error_msg": "El correo electrónico ya está en uso"})

                  form.save()
                  return render(request,"App1/inicio.html" ,  {"mensaje":"Usuario Creado :)"}) and redirect('/')
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"App1/registro.html" ,  {"mensaje":"ERROR","form":form})

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm3(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            #usuario.username = informacion['username']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
           

            usuario.save()

            usuario = request.user 
            email=request.user.email
            fname=request.user.first_name
            lname=request.user.last_name
            miFormulario = UserEditForm()
            return render(request, "App1/miPerfil.html", {"miFormulario": miFormulario, "usuario": usuario,"email": email, "first_name":fname, "last_name":lname, }) and redirect('/verPerfil#card')


    else:

        miFormulario = UserEditForm3()

    return render(request, "App1/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
   
    

@login_required
def cambiarContrasena(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm2(request.POST)
        if miFormulario.is_valid():
            password = miFormulario.cleaned_data['password1']
            usuario.set_password(password)
            usuario.save()
            return render(request, "App1/miPerfil.html", {"usuario": usuario}) and redirect('/exitopass')
    else:
        miFormulario = UserEditForm2()

    return render(request, "App1/cambiarContrasena.html", {"miFormulario": miFormulario, "usuario": usuario})   








def some_view(request):
    user_avatar = Avatar.objects.get(user=request.user)
    return render(request, 'inicio.html', {'user_avatar': user_avatar})

@login_required
def verPerfil(request):
    usuario = request.user 
    email=request.user.email
    fname=request.user.first_name
    lname=request.user.last_name
    miFormulario = UserEditForm()
     
    u = User.objects.get(username=request.user)
    try:
            avatar = Avatar.objects.get(user=u)
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  if avatar is None:
                       avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  else:      
                       avatar.imagen = miFormulario.cleaned_data['imagen']
                  avatar.save()



                  usuario = request.user 
                  email=request.user.email
                  fname=request.user.first_name
                  lname=request.user.last_name
                  miFormulario = UserEditForm()
                  return render(request, "App1/miPerfil.html", {"miFormulario": miFormulario, "usuario": usuario,"email": email, "first_name":fname, "last_name":lname, }) and redirect('/verPerfil#card')

    else: 
            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

    return render(request, "App1/miPerfil.html", {"miFormulario": miFormulario, "usuario": usuario,"email": email, "first_name":fname, "last_name":lname})





def acerca(request):
    return render(request,'App1/acercaDeMi.html')

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
class CalificacionList(ListView):
    model =Calificacion
    template_name='calificacion_list.html'

   
    

from django.views.generic.detail import DetailView
class CalificacionDetalle(DetailView):
    model=Calificacion
    template_name= "calificacion_list.html"

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CalificacionCreacion(LoginRequiredMixin,CreateView):
    model=Calificacion
    success_url="/Calificacion"
    fields= ['usuario','fecha','puntaje','comentario' ]

    def form_valid(self, form):
         form.instance.usuario=self.request.user
         return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['fecha']=date.today().strftime('%d/%m/%Y')
         return context

   
from django.views.generic.edit import UpdateView
class CalificacionUpdate(UpdateView):
    model=Calificacion
    success_url= "/Calificacion"
    fields=['usuario','fecha','puntaje','comentario' ]

from django.views.generic.edit import DeleteView
class CalificacionDelete(LoginRequiredMixin,DeleteView):
    model=Calificacion
    success_url="/Calificacion"   

    """def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['usuario','fecha','puntaje','comentario'].widget.attrs['readonly'] = True
        return form """
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('Inicio')  # Reemplaza 'inicio' con el nombre de tu URL para la página de inicio

        return super().dispatch(request, *args, **kwargs)



"-------------------------------------------------------------------------------------------------"

class DescripcionList(ListView):
    model =Descripcion
    template_name='descripcion_list.html'

class DescripcionDetalle(DetailView):
    model=Descripcion
    template_name= "descripcion_list.html"

class DescripcionCreacion(LoginRequiredMixin,CreateView):
    model=Descripcion
    success_url="/Acerca"
    fields= ['acerca' ]
    """def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['acerca'].widget.attrs['readonly'] = True
        return form """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('Inicio')  # Reemplaza 'inicio' con el nombre de tu URL para la página de inicio

        return super().dispatch(request, *args, **kwargs)


class DescripcionUpdate(UpdateView):
    model=Descripcion
    success_url= "/Acerca"
    fields= ['acerca' ]
    """def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['acerca'].widget.attrs['readonly'] = True
        return form """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('Inicio')  # Reemplaza 'inicio' con el nombre de tu URL para la página de inicio

        return super().dispatch(request, *args, **kwargs)

class DescripcionDelete(LoginRequiredMixin,DeleteView):
    model=Descripcion
    success_url="/Acerca"   
    """def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['acerca'].widget.attrs['readonly'] = True
        return form """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('Inicio')  # Reemplaza 'inicio' con el nombre de tu URL para la página de inicio

        return super().dispatch(request, *args, **kwargs)


"-------------------------------------------------------------------------------------------------"

class ContactoList(ListView):
    model =Contacto
    template_name='contacto_list.html'

class ContactoDetalle(DetailView):
    model=Contacto
    template_name= "contacto_list.html"

class ContactoCreacion(CreateView):
    model=Contacto
    success_url="/exito"
    fields= ['nombre','email','telefono','consulta' ]

    def form_valid(self, form):
        # Guarda el objeto
        self.object = form.save()

        superusers_emails = User.objects.filter(is_superuser=True).values_list('email', flat=True)

        # Envía el correo electrónico
        subject = 'KoyShot Consultas'
        message = 'El Cliente envio la siguiente consulta:\n\n{}'.format(form.cleaned_data)
        from_email = settings.EMAIL_HOST_USER
        #to_email = ['marcosrafaelblanco@gmail.com','marcosblanco.dev@outlook.com']  # dirección de correo del destinatario
        to_email = superusers_emails
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return super().form_valid(form)
    

class ContactoUpdate(UpdateView):
    model=Contacto
    success_url= "/"
    fields= ['nombre','email','telefono','consulta' ] 

class ContactoDelete(LoginRequiredMixin,DeleteView):
    model=Contacto
    success_url="/ContactosList#contact"  

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('Inicio')  # Reemplaza 'inicio' con el nombre de tu URL para la página de inicio

        return super().dispatch(request, *args, **kwargs)
      
    
def exito(request):
    return render(request,'App1/consultaExitosa.html')   

def exitopass(request):
    return render(request,'App1/cambioExitoso.html')   
  
