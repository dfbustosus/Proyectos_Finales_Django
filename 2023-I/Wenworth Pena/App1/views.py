from django.shortcuts import render
from App1.models import *  #Gasto, Ingreso, Trading, Avatar
from django.http import HttpResponse
from App1.forms import * #GastoFormulario, IngresoFormulario, TradingFormulario


from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
@login_required # comnado que requiere login para acceder a esta clase
def gasto(request):
    return render(request,'App1/gastos.html')
@login_required # comnado que requiere login para acceder a esta clase
def ingreso(request):
    return render(request,'App1/ingresos.html')
@login_required # comnado que requiere login para acceder a esta clase
def trading(request):
    return render(request,'App1/tradings.html')
def login(request):
    return render(request,'App1/login.html')
def logout(request):
    return render(request,'App1/logout.html')
def register(request):
    return render(request,'App1/registro.html')
def editarPerfil(request):
    return render(request,'App1/editarPerfil.html')
@login_required # comnado que requiere login para acceder a esta clase
def aboutMe(request):
    return render(request,'App1/aboutMe.html')
def noEnviastesNada(request):
    return render(request,'App1/noEnviastesNada.html')


###gastos POST
def gasto(request):  ######depronto agregar eses ssss a estas funciones
    if request.method =='POST':
        miFormulario=GastoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            gasto=Gasto(int(informacion['id']),str(informacion['fecha']),int(informacion['renta']),
                        int(informacion['alimentacion']),int(informacion['educacion']),
                        int(informacion['transporte']),int(informacion['bills']),
                        int(informacion['vestuario']),int(informacion['recreacion']),
                        int(informacion['otros']))
            gasto.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=GastoFormulario()
    return render(request, 'App1/gastos.html', {"miFormulario": miFormulario})

###ingreso POST
def ingreso(request):
    if request.method =='POST':
        miFormulario=IngresoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            ingreso=Ingreso(int(informacion['id']),str(informacion['fecha']),int(informacion['salario']),
                            int(informacion['part_time']),int(informacion['alquileres']),
                            int(informacion['otros']))
            ingreso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=IngresoFormulario()
    return render(request, 'App1/ingresos.html', {"miFormulario": miFormulario})

###trading POST
def trading(request):
    if request.method =='POST':
        miFormulario=TradingFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            trading=Trading(int(informacion['id']),str(informacion['fecha']),
                            int(informacion['cryptocurrency']),int(informacion['acciones']),
                            int(informacion['otros']))
            trading.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=TradingFormulario()
    return render(request, 'App1/tradings.html', {"miFormulario": miFormulario})

###formularios para enviar informacion
def gastoFormulario(request):
     if request.method == "POST":
        miFormulario = GastoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            gasto = Gasto(int(informacion['id']),str(informacion['fecha']),
                              int(informacion['renta']),int(informacion['alimentacion']), 
                              int(informacion['educacion']),int(informacion['transporte']),
                              int(informacion['bills']),int(informacion['vestuario']),
                              int(informacion['recreacion']),int(informacion['otros']))
            gasto.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = GastoFormulario()
             
     return render(request, "App1/gastoFormulario.html", {"miFormulario": miFormulario})
###formularios para enviar informacion
def ingresoFormulario(request):
     if request.method == "POST":
        miFormulario = IngresoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            ingreso = Ingreso(int(informacion['id']),str(informacion['fecha']),
                              int(informacion['salario']),int(informacion['part_time']), 
                              int(informacion['alquileres']),int(informacion['otros']))
            ingreso.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = IngresoFormulario()
             
     return render(request, "App1/ingresoFormulario.html", {"miFormulario": miFormulario})
###formularios para enviar informacion
def tradingFormulario(request):
     if request.method == "POST":
        miFormulario = TradingFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            trading = Trading(int(informacion['id']),str(informacion['fecha']),
                              int(informacion['cryptocurrency']),int(informacion['acciones']), 
                              int(informacion['otros']))
            trading.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = TradingFormulario()
             
     return render(request, "App1/tradingFormulario.html", {"miFormulario": miFormulario})


###busqueda GASTO REQUEST
@login_required # comnado que requiere login para acceder a esta clase
def busquedaGasto(request):
     return render(request,'App1/busquedaGasto.html')

def buscarGasto(request): #la funcion buscar de cada clase se llama diferente 
     if request.GET['fecha']:
          fecha = request.GET['fecha']
          fechas= Gasto.objects.filter(fecha__icontains=fecha)

          return render(request,'App1/busquedaGasto.html', {"fechas":fechas, "comisiones": fechas })
     else:
          return render(request,'App1/noEnviastesNada.html')

###busqueda Ingreso REQUEST
@login_required # comnado que requiere login para acceder a esta clase
def busquedaIngreso(request):
     return render(request,'App1/busquedaIngreso.html')

def buscarIngreso(request): #la funcion buscar de cada clase se llama diferente 
     if request.GET['fecha']:
          fecha = request.GET['fecha']
          fechas= Ingreso.objects.filter(fecha__icontains=fecha)

          return render(request,'App1/busquedaIngreso.html', {"fechas":fechas, "comisiones": fechas })
     else:
          return render(request,'App1/noEnviastesNada.html')

###busqueda trading REQUEST
@login_required # comnado que requiere login para acceder a esta clase
def busquedaTrading(request):
     return render(request,'App1/busquedaTrading.html')

def buscar(request): #la funcion buscar de cada clase se llama diferente 
     if request.GET['fecha']:
          fecha = request.GET['fecha']
          fechas= Trading.objects.filter(fecha__icontains=fecha)

          return render(request,'App1/busquedaTrading.html', {"fechas":fechas, "comisiones": fechas })
     else:
          return render(request,'App1/noEnviastesNada.html')


###leer, funciones para visualizar toda la informacion de los objetos creados
@login_required # comnado que requiere login para acceder a esta clase
def leerGastos(request):
    gastos= Gasto.objects.all() # trae a todos los gastos
    contexto= {"gastos": gastos}
    return render(request, "App1/leerGastos.html",contexto)
@login_required # comnado que requiere login para acceder a esta clase
def leerIngresos(request):
    ingresos= Ingreso.objects.all() # trae a todos los ingresos
    contexto= {"ingresos": ingresos}
    return render(request, "App1/leerIngresos.html",contexto)
@login_required # comnado que requiere login para acceder a esta clase
def leerTradings(request):
    tradings= Trading.objects.all() # trae a todos los tradings
    contexto= {"tradings": tradings}
    return render(request, "App1/leerTradings.html",contexto)

###delete, funciones para borrar objetos
def eliminarGasto(request, gasto_fecha):
    gasto = Gasto.objects.get(fecha=gasto_fecha)
    gasto.delete()
    # vuelvo al menú
    gastos = Gasto.objects.all()  # trae todos los gastos 
    contexto = {"gastos": gastos}
    return render(request, "App1/leerGastos.html", contexto)

def eliminarIngreso(request, ingreso_fecha):
    ingreso = Ingreso.objects.get(fecha=ingreso_fecha)
    ingreso.delete()
    # vuelvo al menú
    ingresos = Ingreso.objects.all()  # trae todos los ingresos
    contexto = {"ingresos": ingresos}
    return render(request, "App1/leerIngresos.html", contexto)

def eliminarTrading(request, trading_fecha):
    trading = Trading.objects.get(fecha=trading_fecha)
    trading.delete()
    # vuelvo al menú
    tradings = Trading.objects.all()  # trae todos los tradings
    contexto = {"tradings": tradings}
    return render(request, "App1/leerTradings.html", contexto)

###update funciones para actualizar objetos de la clase Gastos
def editarGasto(request, gasto_fecha):
    # Recibe la fecha de gasto que vamos a modificar
    gasto = Gasto.objects.get(fecha=gasto_fecha)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = GastoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            gasto.fecha = informacion['fecha']
            gasto.renta = informacion['renta']
            gasto.alimentacion = informacion['alimentacion']
            gasto.educacion = informacion['educacion']
            gasto.transporte = informacion['transporte']
            gasto.bills = informacion['bills']
            gasto.vestuario = informacion['vestuario']
            gasto.recreacion = informacion['recreacion']
            gasto.otros = informacion['otros']
            gasto.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "App1/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = GastoFormulario(initial={'fecha': gasto.fecha, 'renta': gasto.renta,
                                                   'alimentacion': gasto.alimentacion, 'educacion': gasto.educacion,
                                                   'transporte': gasto.transporte, 'bills': gasto.bills,
                                                   'vestuario': gasto.vestuario, 'recreacion': gasto.recreacion,
                                                   'otros': gasto.otros})
    # Voy al html que me permite editar
    return render(request, "App1/editarGasto.html", {"miFormulario": miFormulario, "gasto_fecha": gasto_fecha})

###update funciones para actualizar objetos de la clase ingreso
def editarIngreso(request, ingreso_fecha):
    # Recibe la fecha  de ingreso que vamos a modificar
    ingreso = Ingreso.objects.get(fecha=ingreso_fecha)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = IngresoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            ingreso.fecha = informacion['fecha']
            ingreso.salario = informacion['salario']
            ingreso.part_time = informacion['part_time']
            ingreso.alquileres = informacion['alquileres']
            ingreso.otros = informacion['otros']
            ingreso.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "App1/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = IngresoFormulario(initial={'fecha': ingreso.fecha, 'salario': ingreso.salario,
                                                   'part_time': ingreso.part_time, 'alquileres': ingreso.alquileres,
                                                   'otros': ingreso.otros})        
    # Voy al html que me permite editar
    return render(request, "App1/editarIngreso.html", {"miFormulario": miFormulario, "ingreso_fecha": ingreso_fecha})

###update funciones para actualizar objetos de la clase Trading
def editarTrading(request, trading_fecha):
    # Recibe la fecha de trading que vamos a modificar
    trading = Trading.objects.get(fecha=trading_fecha)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = TradingFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            trading.fecha = informacion['fecha']
            trading.cryptocurrency = informacion['cryptocurrency']
            trading.acciones = informacion['acciones']
            trading.otros = informacion['otros']
            trading.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "App1/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = TradingFormulario(initial={'fecha': trading.fecha, 'cryptocurrency': trading.cryptocurrency,
                                                   'acciones': trading.acciones, 'otros': trading.otros})        
    # Voy al html que me permite editar
    return render(request, "App1/editarTrading.html", {"miFormulario": miFormulario, "trading_fecha": trading_fecha})

###-------CRUD
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
###-------Gasto CRUD
### EL PROGRAMA NO DEJA HACER CRUD A LAS TRES CLASES, TODAS ESTAN FUNCIONANDO, PERO SOLO
### SE PUEDE PROBAR UNA A LA VEZ
### realizando CRUD, Create, Read, Update and Delete, 
'''
class GastoList(ListView):
    model =Gasto
    template_name='/App1/gasto_list.html'

class GastoDetalle(DetailView):
    model=Gasto
    template_name= "App1/gasto_detalle.html"

class GastoCreacion(CreateView):
    model=Gasto
    success_url="/App1/gasto/list"
    fields= ['fecha','renta','alimentacion','educacion','transporte','bills','vestuario',
             'recreacion','otros']

class GastoUpdate(UpdateView):
    model=Gasto
    success_url= "/App1/gasto/list"
    fields=['fecha','renta','alimentacion','educacion','transporte','bills','vestuario',
             'recreacion','otros']

class GastoDelete(DeleteView):
    model=Gasto
    success_url="/App1/gasto/list"   
'''
###-------Ingreso CRUD
### EL PROGRAMA NO DEJA HACER CRUD A LAS TRES CLASES, TODAS ESTAN FUNCIONANDO, PERO SOLO
### SE PUEDE PROBAR UNA A LA VEZ
### realizando CRUD, Create, Read, Update and Delete, 
###ingreso  /// clases basadas en vistas CBV, App1/ingreso/list
'''
class IngresoList(ListView):
    model =Ingreso
    template_name='/App1/ingreso_list.html'

class IngresoDetalle(DetailView):
    model=Ingreso
    template_name= "App1/ingreso_detalle.html"

class IngresoCreacion(CreateView):
    model=Ingreso
    success_url="/App1/ingreso/list"
    fields= ['fecha','salario','part_time','alquileres','otros']

class IngresoUpdate(UpdateView):
    model=Ingreso
    success_url= "/App1/ingreso/list"
    fields=['fecha','salario','part_time','alquileres','otros']

class IngresoDelete(DeleteView):
    model=Ingreso
    success_url="/App1/ingreso/list"
'''
###-------Trading CRUD
### EL PROGRAMA NO DEJA HACER CRUD A LAS TRES CLASES, TODAS ESTAN FUNCIONANDO, PERO SOLO
### SE PUEDE PROBAR UNA A LA VEZ
### realizando CRUD, Create, Read, Update and Delete, 
###trading  /// clases basadas en vistas CBV, App1/trading/list
class TradingList(ListView):
    model =Trading
    template_name='/App1/trading_list.html'

class TradingDetalle(DetailView):
    model=Trading
    template_name= "App1/trading_detalle.html"

class TradingCreacion(CreateView):
    model=Trading
    success_url="/App1/trading/list"
    fields= ['fecha','cryptocurrency','acciones','otros']

class TradingUpdate(UpdateView):
    model=Trading
    success_url= "/App1/trading/list"
    fields=['fecha','cryptocurrency','acciones','otros']

class TradingDelete(DeleteView):
    model=Trading
    success_url="/App1/trading/list"

###login, App1/login
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
                return render(request, "App1/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "App1/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "App1/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "App1/login.html", {"form": form}) 

###register, App1/register
from App1.forms import UserRegisterForm
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

###MyMixin, App1/my-protected-page/, primero hay que hacer logout, luego entramos 
# aqui App1/my-protected-page/ y luego la pagina nos pidira logiarnos para poder acceder a la info
class MyMixin:
    def my_method(self):
        return "Hello from MyMixin!"

from django.views.generic import TemplateView

class MyView(MyMixin, TemplateView):
    template_name = "App1/protected.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = self.my_method()
        return context
    

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class MyProtectedView(MyMixin, LoginRequiredMixin, TemplateView):
    template_name = "App1/protected1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = self.my_method()
        return context

# Vista de editar el perfil, App1/editarPerfil
from App1.forms import UserRegisterForm, UserEditForm
@login_required  #para editar perfil, primero hay que estar logeado
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

###funcion Avatar
#from App1.models import Avatar #esta clase ya esta habilitada al inicio de este archivo
@login_required
def inicio(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    return render(request, 'App1/inicio.html', {"url":avatares[0].imagen.url})

#con esta funcion ubicamos el Avatar en otro lugar de la pagina de inicio
#from App1.models import Avatar  #esta clase ya esta habilitada al inicio de este archivo
def some_view(request):
    user_avatar = Avatar.objects.get(user=request.user)
    return render(request, 'padre.html', {'user_avatar': user_avatar})

###funcion que interactua con la funcion que esta en forms.py para crear un formulario de Avatars
from django.contrib.auth.models import User
from .forms import AvatarFormulario
@login_required  ### para poder obtener un Avatar hay que estar logeado
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "App1/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= AvatarFormulario() #Formulario vacio para construir el html
      return render(request, "App1/agregarAvatar.html", {"miFormulario":miFormulario})



