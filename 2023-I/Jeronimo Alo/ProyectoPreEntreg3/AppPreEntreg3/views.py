from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from AppPreEntreg3.models import ProdRemera, ProdBuzo, ProdPantalon, Avatar, User
from AppPreEntreg3.forms import RemerasForm, BuzosForm, PantalonesForm, UserRegisterForm, UserEditForm, AvatarFormulario
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password

def superadmin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, "AppPreEntreg3/inicio.html", {"mensaje5":"No eres superadmin, por favor logueate como tal"})
        return view_func(request, *args, **kwargs)
    return wrapper

# Create your views here.

def inicio(request):
    return render(request, 'AppPreEntreg3/inicio.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "AppPreEntreg3/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "App1/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "AppPreEntreg3/login.html", {"mensaje":"Usuario o Contraseña Incorrectos", "form": form})
    form = AuthenticationForm()
    return render(request, "AppPreEntreg3/login.html", {"form": form})

def register(request):
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppPreEntreg3/inicio.html" ,  {"mensaje":"Usuario Creado, por favor inicie sesión"})
      else:   
            form = UserRegisterForm()     
      return render(request,"AppPreEntreg3/registro.html" ,  {"form":form})

def aboutme(request):
    return render(request, 'AppPreEntreg3/aboutme.html')

@login_required
def remeras(request):
    remeras = ProdRemera.objects.all() # trae todas las remeras.
    contexto= {"remeras": remeras}
    return render(request, 'AppPreEntreg3/remeras.html', contexto)

@login_required
def buzos(request):
    buzos = ProdBuzo.objects.all() # trae todos los buzos.
    contexto= {"buzos": buzos}
    return render(request, 'AppPreEntreg3/buzos.html', contexto)

@login_required
def pantalones(request):
    pantalones = ProdPantalon.objects.all() # trae todos los pantalones.
    contexto= {"pantalones": pantalones}
    return render(request, 'AppPreEntreg3/pantalones.html', contexto)

@login_required
def busquedaRemera(request):
     return render(request,'AppPreEntreg3/busquedaRemera.html')

@login_required
def busquedaBuzo(request):
     return render(request,'AppPreEntreg3/busquedaBuzo.html')

@login_required
def busquedaPantalon(request):
     return render(request,'AppPreEntreg3/busquedaPantalon.html')

@login_required
@superadmin_required
def remerasForm(request):
    if request.method == "POST":
        miFormulario = RemerasForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            remeras = ProdRemera(int(informacion['id']),str(informacion['nombre']),str(informacion['tamaño']), 
                                 informacion['color'], float(informacion['precio']), int(informacion['stock']))
            remeras.save()
            return render(request, "AppPreEntreg3/inicio.html")
    else:
        miFormulario = RemerasForm() #Formulario vacío.
             
    return render(request, "AppPreEntreg3/remerasForm.html", {"miFormulario": miFormulario})

@login_required
@superadmin_required
def buzosForm(request):
    if request.method == "POST":
        miFormulario = BuzosForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            buzos = ProdBuzo(int(informacion['id']),str(informacion['nombre']),str(informacion['tamaño']), 
                                 informacion['color'], float(informacion['precio']), int(informacion['stock']))
            buzos.save()
            return render(request, "AppPreEntreg3/inicio.html")
    else:
        miFormulario = BuzosForm() #Formulario vacío.
             
    return render(request, "AppPreEntreg3/buzosForm.html", {"miFormulario": miFormulario})

@login_required
@superadmin_required
def pantalonesForm(request):
    if request.method == "POST":
        miFormulario = PantalonesForm(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            pantalones = ProdPantalon(int(informacion['id']),str(informacion['nombre']),str(informacion['tamaño']), 
                                 informacion['color'], informacion['diseño'], float(informacion['precio']), int(informacion['stock']))
            pantalones.save()
            return render(request, "AppPreEntreg3/inicio.html")
    else:
        miFormulario = PantalonesForm() #Formulario vacío.
             
    return render(request, "AppPreEntreg3/pantalonesForm.html", {"miFormulario": miFormulario})

@login_required
def buscarRem(request):
    if request.GET['remera']:
        remera = request.GET['remera']
        remeras = ProdRemera.objects.filter(nombre__icontains=remera)

        return render(request,'AppPreEntreg3/resultadosRemeras.html', {"remeras":remeras, "remera": remera })
    else:
        respuesta= "No enviaste datos"

    return render(request,"AppPreEntreg3/inicio.html",{"respuesta":respuesta})

@login_required
def buscarBuzo(request):
    if request.GET['buzo']:
        buzo = request.GET['buzo']
        buzos = ProdBuzo.objects.filter(nombre__icontains=buzo)

        return render(request,'AppPreEntreg3/resultadosBuzos.html', {"buzos":buzos, "buzo": buzo })
    else:
        respuesta= "No enviaste datos"

    return render(request,"AppPreEntreg3/inicio.html",{"respuesta":respuesta})

@login_required
def buscarPant(request):
    if request.GET['pantalon']:
        pantalon = request.GET['pantalon']
        pantalones = ProdPantalon.objects.filter(nombre__icontains=pantalon)

        return render(request,'AppPreEntreg3/resultadosPantalones.html', {"pantalones":pantalones, "pantalon": pantalon })
    else:
        respuesta= "No enviaste datos"

    return render(request,"AppPreEntreg3/inicio.html",{"respuesta":respuesta})

@login_required
@superadmin_required
def editarRem(request, remera_nombre):
    remera = ProdRemera.objects.get(nombre=remera_nombre)
    # Si es metodo POST...
    if request.method == 'POST':
        miFormulario = RemerasForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            remera.nombre = informacion['nombre']
            remera.tamaño = informacion['tamaño']
            remera.color = informacion['color']
            remera.precio = informacion['precio']
            remera.stock = informacion['stock']
            remera.save()

            # Vuelvo al inicio.
            return render(request, "AppPreEntreg3/inicio.html")
    # En caso que no sea post...
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = RemerasForm(initial={'nombre': remera.nombre, 'tamaño': remera.tamaño,
                                                'color': remera.color, 'precio': remera.precio, 'stock': remera.stock})
    # Voy al html que me permite editar
    return render(request, "AppPreEntreg3/editarRemera.html", {"miFormulario": miFormulario, "remera_nombre": remera_nombre})

@login_required
@superadmin_required
def editarBuzo(request, buzo_nombre):
    buzo = ProdBuzo.objects.get(nombre=buzo_nombre)
    # Si es metodo POST...
    if request.method == 'POST':
        miFormulario = BuzosForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            buzo.nombre = informacion['nombre']
            buzo.tamaño = informacion['tamaño']
            buzo.color = informacion['color']
            buzo.precio = informacion['precio']
            buzo.stock = informacion['stock']
            buzo.save()

            # Vuelvo al inicio.
            return render(request, "AppPreEntreg3/inicio.html")
    # En caso que no sea post...
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = BuzosForm(initial={'nombre': buzo.nombre, 'tamaño': buzo.tamaño,
                                                'color': buzo.color, 'precio': buzo.precio, 'stock': buzo.stock})
    # Voy al html que me permite editar
    return render(request, "AppPreEntreg3/editarBuzo.html", {"miFormulario": miFormulario, "buzo_nombre": buzo_nombre})

@login_required
@superadmin_required
def editarPant(request, pantalon_nombre):
    pantalon = ProdPantalon.objects.get(nombre=pantalon_nombre)
    # Si es metodo POST...
    if request.method == 'POST':
        miFormulario = PantalonesForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            pantalon.nombre = informacion['nombre']
            pantalon.tamaño = informacion['tamaño']
            pantalon.color = informacion['color']
            pantalon.diseño = informacion['diseño']
            pantalon.precio = informacion['precio']
            pantalon.stock = informacion['stock']
            pantalon.save()

            # Vuelvo al inicio.
            return render(request, "AppPreEntreg3/inicio.html")
    # En caso que no sea post...
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = PantalonesForm(initial={'nombre': pantalon.nombre, 'tamaño': pantalon.tamaño,
                                                'color': pantalon.color, 'diseño':pantalon.diseño, 'precio': pantalon.precio, 'stock': pantalon.stock})
    # Voy al html que me permite editar
    return render(request, "AppPreEntreg3/editarPantalon.html", {"miFormulario": miFormulario, "pantalon_nombre": pantalon_nombre})

@login_required
@superadmin_required
def eliminarRem(request, remera_nombre):
    remera = ProdRemera.objects.get(nombre=remera_nombre)
    remera.delete()

    #Volvemos al inicio.
    return render(request, "AppPreEntreg3/inicio.html")

@login_required
@superadmin_required
def eliminarBuzo(request, buzo_nombre):
    buzo = ProdBuzo.objects.get(nombre=buzo_nombre)
    buzo.delete()

    #Volvemos al inicio.
    return render(request, "AppPreEntreg3/inicio.html")

@login_required
@superadmin_required
def eliminarPant(request, pantalon_nombre):
    pantalon = ProdPantalon.objects.get(nombre=pantalon_nombre)
    pantalon.delete()

    #Volvemos al inicio.
    return render(request, "AppPreEntreg3/inicio.html")

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            password1 = informacion['password1']
            password2 = informacion['password2']

            if password1 and password1 == password2:
                usuario.password = make_password(password1)

            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "AppPreEntreg3/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "AppPreEntreg3/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

def some_view(request):
    user_avatar = Avatar.objects.get(user=request.user)
    return render(request, 'padre.html', {'user_avatar': user_avatar})

@login_required
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí llega toda la información del html.
            if miFormulario.is_valid():   #Si pasó la validación de Django
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "AppPreEntreg3/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= AvatarFormulario() #Formulario vacio para construir el html.
      return render(request, "AppPreEntreg3/agregarAvatar.html", {"miFormulario":miFormulario})