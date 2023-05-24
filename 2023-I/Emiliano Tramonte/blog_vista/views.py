from django.shortcuts import render
from blog_vista.models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

#vistas principales de los models
from django.templatetags.static import static

def my_view(request):
    background_image_url = static('blog_vista/assets/img/home-bg.jpg')
    return render(request, 'padre.html', {'background_image_url': background_image_url})

def inicio(request):  
    return render (request, 'blog_vista/inicio.html')

def about(request):
    return render (request, 'blog_vista/about.html')
login_required
def medicina(request):
    return render (request, 'blog_vista/medicina.html') 
login_required
def biologia (request):
    return render (request, 'blog_vista/biologia.html')
login_required
def filosofia (request):
    return render (request, 'blog_vista/filosofia.html')
login_required
def astronomia(request):
    return render (request, 'blog_vista/astronomia.html')
login_required
def tecnologia (request):
    return render (request, 'blog_vista/tecnologia.html')
login_required
def miembros (request):
    return render (request, 'blog_vista/miembros.html')




#vistas en listas y detalles de cada model
from django.views.generic import ListView
from django.views.generic.detail import DetailView

class MedicinaList(ListView):
    model = Medicina 
    template_name='/blog_vista/medicina_list.html'

class AstronomiaList(ListView):
    model = Astronomía
    template_name = 'blog_vista/astronomia_list.html'

class FilosofiaList(ListView):
    model = Filosofía
    template_name = 'blog_vista/filosofia_list.html'


class MedicinaDetalle(DetailView):
    model= Medicina
    template_name= "blog_vista/medicina_detalle.html"


def detalle_astronomia(request, pk):

    astronomia = Astronomía.objects.get(pk=pk)
    contexto = {'astronomia': astronomia}
    return render(request, 'blog_vista/astronomia_detalle.html', contexto)

def detalle_filosofia(request, pk):
    filosofia = Filosofía.objects.get(pk=pk)
    contexto = {'filosofia': filosofia}
    return render(request, 'blog_vista/filosofia_detalle.html', contexto)

class BiologiaList(ListView):
    model = Biología
    template_name = 'blog_vista/biologia_list.html'

def detalle_biologia(request, pk):
    biologia = Biología.objects.get(pk=pk)
    contexto = {'biologia': biologia}
    return render(request, 'blog_vista/biologia_detalle.html', contexto)

class TecnologiaList(ListView):
    model = Tecnología
    template_name = 'blog_vista/tecnologia_list.html'


def detalle_tecnologia(request, pk):
    tecnologia = Tecnología.objects.get(pk=pk)
    contexto = {'tecnologia': tecnologia}
    return render(request, 'blog_vista/tecnologia_detalle.html', contexto)

class MiembrosList(ListView):
    model = Miembros
    template_name = 'blog_vista/miembros_list.html'


class MiembrosDetalle(DetailView):
    model = Miembros
    template_name = 'blog_vista/miembros_detalle.html'

#vistas de los forms: 
from django import forms
from .forms import *

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def miembros_form(request): 
    if request.method == 'POST':
        #form = MiembrosForm(request.POST)
        form = MiembrosForm(request.POST, request.FILES)

        if form.is_valid(): 
            informacion = form.cleaned_data
            miembro = Miembros(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], universidad=informacion['universidad'], foto=informacion['foto'])
            miembro.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = MiembrosForm()
        
    return render(request, 'blog_vista/miembros_form.html', {'form': form})

@staff_member_required
def medicina_form(request): 
    if request.method == 'POST':
        form = MedicinaForm(request.POST, request.FILES)

        if form.is_valid(): 
            informacion = form.cleaned_data
            articulo_medicina = Medicina(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], autor=informacion['autor'], imagen=informacion['imagen'])
            articulo_medicina.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = MedicinaForm()
        
    return render(request, 'blog_vista/medicina_form.html', {'form': form})

@staff_member_required
def filosofia_form(request): 
    if request.method == 'POST':
        form = FilosofiaForm(request.POST, request.FILES)

        if form.is_valid(): 
            informacion = form.cleaned_data
            articulo_filosofia = Filosofía(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], autor=informacion['autor'], imagen=informacion['imagen'])
            articulo_filosofia.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = FilosofiaForm()
        
    return render(request, 'blog_vista/filosofía_form.html', {'form': form})

@staff_member_required
def biologia_form(request): 
    if request.method == 'POST':
        form = BiologiaForm(request.POST, request.FILES)

        if form.is_valid(): 
            informacion = form.cleaned_data
            articulo_biologia = Biología(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], autor=informacion['autor'], imagen=informacion['imagen'])
            articulo_biologia.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = BiologiaForm()
        
    return render(request, 'blog_vista/biología_form.html', {'form': form})

@staff_member_required
def astronomia_form(request): 
    if request.method == 'POST':
        form = AstronomiaForm(request.POST, request.FILES)

        if form.is_valid(): 
            informacion = form.cleaned_data
            articulo_astronomia = Astronomía(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], autor=informacion['autor'], imagen=informacion['imagen'])
            articulo_astronomia.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = AstronomiaForm()
        
    return render(request, 'blog_vista/astronomía_form.html', {'form': form})

@staff_member_required
def tecnologia_form(request): 

    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)

        if form.is_valid(): 
            informacion = form.cleaned_data
            articulo_tecnologia = Tecnología(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], texto=informacion['texto'], autor=informacion['autor'], imagen=informacion['imagen'])
            articulo_tecnologia.save()
            return render(request, 'blog_vista/inicio.html')
        else:
            print(form.errors)
    
    else:
        form = TecnologiaForm()
        
    return render(request, 'blog_vista/tecnología_form.html', {'form': form})

#vistas de edicion

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class InicioView(TemplateView):
    template_name = 'blog_vista/inicio.html'

def user_is_admin(user):
    return user.is_superuser

@method_decorator(staff_member_required, name='dispatch')
class MiembrosUpdate(UpdateView):
    model = Miembros
    success_url = reverse_lazy('MiembrosList')
    fields = ['nombre', 'apellido', 'email', 'universidad', 'foto']

@method_decorator(staff_member_required, name='dispatch')
class MiembrosDelete(DeleteView):
    model = Miembros
    success_url = reverse_lazy('MiembrosList')

@method_decorator(staff_member_required, name='dispatch')
class AstronomiaUpdate(UpdateView):
    model = Astronomía
    success_url = reverse_lazy('AstronomiaList')
    fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']

@method_decorator(staff_member_required, name='dispatch')
class AstronomiaDelete(DeleteView):
    model = Astronomía
    success_url = reverse_lazy('AstronomiaList')

@method_decorator(staff_member_required, name='dispatch')
class BiologiaUpdate(UpdateView):
    model = Biología
    success_url = reverse_lazy('BiologiaList')
    fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']

@method_decorator(staff_member_required, name='dispatch')
class BiologiaDelete(DeleteView):
    model = Biología
    success_url = reverse_lazy('BiologiaList')

@method_decorator(staff_member_required, name='dispatch')
class MedicinaUpdate(UpdateView):
    model = Medicina
    success_url = reverse_lazy('MedicinaList')
    fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']

@method_decorator(staff_member_required, name='dispatch')
class MedicinaDelete(DeleteView):
    model = Medicina
    success_url = reverse_lazy('MedicinaList')

@method_decorator(staff_member_required, name='dispatch')
class FilosofiaUpdate(UpdateView):
    model = Filosofía
    success_url = reverse_lazy('FilosofiaList')
    fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']

@method_decorator(staff_member_required, name='dispatch')
class FilosofiaDelete(DeleteView):
    model = Filosofía
    success_url = reverse_lazy('FilosofiaList')

@method_decorator(staff_member_required, name='dispatch')
class TecnologiaUpdate(UpdateView):
    model = Tecnología
    success_url = reverse_lazy('TecnologiaList')
    fields = ['titulo', 'subtitulo', 'texto', 'autor', 'imagen']

@method_decorator(staff_member_required, name='dispatch')
class TecnologiaDelete(DeleteView):
    model = Tecnología
    success_url = reverse_lazy('TecnologiaList')

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login,logout,authenticate


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "blog_vista/inicio.html", {"mensaje":f"{usuario}, es tu momento de navegar en el efecto doppler!"})
            else:
                return render(request, "blog_vista/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "blog_vista/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "blog_vista/login.html", {"form": form})

from blog_vista.forms import UserRegisterForm
def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"blog_vista/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"blog_vista/registro.html" ,  {"form":form})

from blog_vista.forms import UserRegisterForm, UserEditForm
# Vista de editar el perfil
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            
            usuario.save()
            return render(request, "blog_vista/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "blog_vista/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


@login_required
def profile(request):

    usuario = request.user
    context = {'usuario': usuario}
    return render(request, 'blog_vista/profile.html', context)

@login_required
def inicio_login(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    return render(request, 'blog_vista/inicio.html', {"url":avatares[-1].imagen.url})

def some_view(request):
    user_avatar = Avatar.objects.get(user=request.user)
    return render(request, 'blog_vista/padre.html', {'user_avatar': user_avatar})


@login_required
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():  
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "blog_vista/inicio.html") 
      else: 
            miFormulario= AvatarFormulario() 
      return render(request, "blog_vista/agregarAvatar.html", {"miFormulario":miFormulario})

