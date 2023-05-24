from django.shortcuts import render
#from django.template import loader 
from .models import Acceso, Servicios, Freelance, Contratador, Avatar
from .forms import freelanceFormulario, contratadorFormulario, serviciosFormulario, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login,logout,authenticate
from App1.forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def inicio(request):
    return render (request,"App1/inicio.html")
def Acceso(request):
    return render (request,"App1/Acceso.html")
def Freelance(request):
    return render (request,"App1/Freelance.html")
def Contratador(request):
    return render (request,"App1/Contratador.html")
def Servicios(request):
    return render (request,"App1/Servicios.html")

def freelance_view(request):
      if request.method == "POST":
            miFormulario = freelanceFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  Freelance =  Freelance(int(informacion['id']),str(informacion['nombre']),str(informacion['mail']),str(informacion['profesion']),str(informacion['servicios']))
                  Freelance.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = freelanceFormulario()
 
      return render(request, "App1/Freelance.html", {"miFormulario": miFormulario})


def contratador_view (request):
     if request.method == "POST":
        miFormulario = contratadorFormulario(request.POST) 
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            Contratador = Contratador(int(informacion['id']),str(informacion['nombre']),str(informacion['mail']),str(informacion['profesion']),str(informacion['servicios']))
            Contratador.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = contratadorFormulario()
             
     return render(request, "App1/Contratador.html", {"miFormulario": miFormulario})

def servicios_view (request):
     if request.method == "POST":
        miFormulario = serviciosFormulario(request.POST) 
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            Servicios = Servicios(int(informacion['id']),str(informacion['nombreServicio']),str(informacion['rubro']))
            Servicios.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = serviciosFormulario()
             
     return render(request, "App1/Servicios.html", {"miFormulario": miFormulario})

def busquedaFreelance(request):
     return render(request,'App1/busquedaFreelance.html')

def buscar(request):
     if request.GET['Freelance']:
          Freelance = request.GET['Freelance']
          Freelance = Freelance.objects.filter(Freelance__icontains=Freelance)

          return render(request,'App1/inicio.html', {"nombre":Freelance, "mail": Freelance })
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)


def leerFreelance_view(request):
    Freelances= Freelance.objects.all()     
    contexto= {"Freelance": Freelances}
    return render(request, "App1/leerFreelance.html",contexto)

def leerContratador_view (request):
    Contratadores= Contratador.objects.all()     
    contexto= {"Contratador": Contratadores}
    return render(request, "App1/leerContratador.html",contexto)

def leerServicios_view (request):
    Servicio= Servicios.objects.all()     
    contexto= {"Servicios": Servicio}
    return render(request, "App1/leerServicios.html",contexto)

def eliminarFreelance(request, freelance_nombre):
    Freelances = Freelance.objects.get(nombre=freelance_nombre)
    Freelance.delete()
    
    Freelance = Freelance.objects.all()   
    contexto = {"Freelance": Freelances}
    return render(request, "App1/leerFreelance.html", contexto)

def eliminarContratador(request, contratador_nombre):
    Contratadores = Contratador.objects.get(nombre=contratador_nombre)
    Contratador.delete()
    
    Contratador = Contratador.objects.all()   
    contexto = {"Contratador": Contratadores}
    return render(request, "App1/leerContratador.html", contexto)

def eliminarServicios(request, servicio_nombreServicio):
    Servicio = Servicios.objects.get(nombre=servicio_nombreServicio)
    Servicios.delete()
    
    Servicios = Servicios.objects.all()   
    contexto = {"Servicios": Servicio}
    return render(request, "App1/leerServicios.html", contexto)

def editarFreelance(request, freelance_nombre):
    Freelance = Freelance.objects.get(nombre=freelance_nombre)
    if request.method == 'POST':
        miFormulario = freelanceFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            Freelance.nombre = informacion['nombre']
            Freelance.apellido = informacion['apellido']
            Freelance.email = informacion['email']
            Freelance.profesion = informacion['profesion']
            Freelance.servicios = informacion['servicios']
            Freelance.save()

            return render(request, "App1/inicio.html")
        
        return render(request, "App1/editarFreelance.html", {"miFormulario": miFormulario, "freelance_nombre":freelance_nombre})

def editarContratador(request, contratador_nombre):
    Freelance = Freelance.objects.get(nombre=contratador_nombre)
    if request.method == 'POST':
        miFormulario = contratadorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            Contratador.nombre = informacion['nombre']
            Contratador.apellido = informacion['apellido']
            Contratador.email = informacion['email']
            Contratador.profesion = informacion['profesion']
            Contratador.servicios = informacion['servicios']
            Contratador.save()

            return render(request, "App1/inicio.html")
        
        return render(request, "App1/editarContratador.html", {"miFormulario": miFormulario, "contratador_nombre":contratador_nombre})

def editarServicios(request, servicio_nombreServicio):
    Freelance = Freelance.objects.get(nombre=servicio_nombreServicio)
    if request.method == 'POST':
        miFormulario = serviciosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            Servicios.nombreServicio = informacion['nombreServicio']
            Servicios.rubro = informacion['rubro']
            Servicios.save()

            return render(request, "App1/inicio.html")
        
        return render(request, "App1/editarServicios.html", {"miFormulario": miFormulario, "servicio_nombreServicio": servicio_nombreServicio})

class FreelanceList(ListView):
    model=Freelance 
    template_name= "App1/freelance_list.html"

class FreelanceDetalle(DetailView):
    model=Freelance 
    template_name= "App1/freelance_detalle.html"

class FreelanceCreacion(CreateView):
    model= Freelance
    success_url="/App1/Freelance/list"
    fields= ['nombre','apellido','mail','profesion', 'servicios']

class FreelanceUpdate(UpdateView):
    model= Freelance
    success_url="/App1/Freelance/list"
    fields= ['nombre','apellido','mail','profesion', 'servicios']

class FreelanceDelete(DeleteView):
    model= Freelance
    success_url="/App1/Freelance/list"

class ContratadorList(ListView):
    model=Contratador 
    template_name= "App1/contratador_list.html"

class ContratadorDetalle(DetailView):
    model=Contratador 
    template_name= "App1/contratador_detalle.html"

class ContratadorCreacion(CreateView):
    model= Contratador
    success_url="/App1/Contratador/list"
    fields= ['nombre','apellido','mail','profesion', 'servicios']

class ContratadorUpdate(UpdateView):
    model= Contratador
    success_url="/App1/Contratador/list"
    fields= ['nombre','apellido','mail','profesion', 'servicios']

class ContratadorDelete(DeleteView):
    model= Contratador
    success_url="/App1/Contratador/list"

class ServiciosList(ListView):
    model=Contratador 
    template_name= "App1/servicios_list.html"

class ServiciosDetalle(DetailView):
    model=Contratador 
    template_name= "App1/servicios_detalle.html"

class ServiciosCreacion(CreateView):
    model= Servicios
    success_url="/App1/Servicios/list"
    fields= ['nombreServicio','rubro']

class ServiciosUpdate(UpdateView):
    model= Servicios
    success_url="/App1/Servicios/list"
    fields= ['nombreServicio','rubro']

class ServiciosDelete(DeleteView):
    model= Servicios
    success_url="/App1/Servicios/list"

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "App1/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "App1/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "App1/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "App1/login.html", {"form": form})


def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"App1/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"App1/registro.html" ,  {"form":form})


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
            return render(request, "App1/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "App1/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

def inicio(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    return render(request, 'App1/inicio.html', {"url":avatares[0].imagen.url})

from django.views.generic import TemplateView

class MyMixin:
    def my_method(self):
        return "Hello from MyMixin!"
    
class MyProtectedView(MyMixin, LoginRequiredMixin, TemplateView):
    template_name = "App1/protected1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = self.my_method()
        return context
