from django.shortcuts import render, get_object_or_404
from .forms import ClientForm, ProductoForm, SellerForm, AvatarFormulario
from .models import Clients, Products, Sellers, Avatar
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# from PIL import Image, ImageChops, ImageEnhance, ImageOps
from django.http import HttpResponse


# Create your views here.

def home(request):
        
    return render(request, "./app/base.html", {'active_view': 'vista_home'})

def profile(request):

    return render(request, "./app/profile.html", {'active_view': 'vista_profile'})

def registro(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password-confirm']

        if password != password_confirm:
            messages.success(request, 'Las contraseñas no coinciden', extra_tags='danger')
            return render(request, './app/registro.html', {'active_view': 'vista_registro'})

        else:
            user = User.objects.create_user(username, email, password)
            user.is_staff = True
            user.save()
            messages.success(request, 'El Usuario se ha creado con exito')
    
    return render(request, './app/registro.html', {'active_view': 'vista_registro'})

def logeo(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if authenticate:
            try:
                login(request, user)
            except:
                messages.success(request, 'Ha ocurrido un error', extra_tags='danger')
            else:
                messages.success(request, 'Se ha logeado exotisamente')
            
    return render(request, './app/logeo.html', {'active_view': 'vista_login'})

def desloguear(request):

    logout(request)
    return render(request, './app/home.html', {'active_view': 'vista_logout'})

@login_required(login_url='/logeo/')
def client(request):

    request.method == 'GET'
    clientes = Clients.objects.all()

    if request.method =='POST':
        form = ClientForm(request.POST)

        if form.is_valid:
            form.save()
            messages.success(request, 'El cliente se ha creado con éxito.')
            form = ClientForm()
            return render(request, './app/cliente.html', {'form': form, 'clientes': clientes, 'active_view': 'vista_clientes'})
    else:
        form = ClientForm()
    return render(request, './app/cliente.html', {'form': form, 'clientes': clientes, 'active_view': 'vista_clientes'})

@login_required(login_url='/logeo/')
def cliente_editar(request, id_cliente):

    client = Clients.objects.get(id=id_cliente)
    
    if(request.method == 'GET'):
        form = ClientForm(instance=client)
        return render(request, './app/cliente_editar.html', {"form": form, 'client': client, 'active_view': 'vista_clientes'})
        

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)

        if form.is_valid:
            form.save()
            messages.success(request,'el Cliente se ha editado exitosamente.')
            return render(request, "./app/cliente_editar.html", {'active_view': 'vista_clientes'})
        
        else:
            messages.success(request,'Hubo un erro al intentar editar el Cliente.')
            return render(request, "./app/cliente.html", {'active_view': 'vista_clientes'})

@login_required(login_url='/logeo/')
def cliente_eliminar(request, id_cliente):

    if(request.method == 'GET'):
        client = Clients.objects.get(id=id_cliente)
        client.delete()
        messages.success(request,'el Cliente se ha eliminado exitosamente.')
        return render(request, './app/cliente_eliminar.html', {'active_view': 'vista_clientes'})
    else:
        messages.success(request,'Hubo un erro al intentar borrar el Cliente.')
        return render(request, './app/cliente_eliminar.html', {'active_view': 'vista_clientes'})

@login_required(login_url='/logeo/')
def product(request):

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'El producto se ha creado con éxito.')
            form = ProductoForm()
    else:
        form = ProductoForm(initial={'image': 'default_image.jpg'})

    productos = Products.objects.all()
    return render(request, './app/producto.html', {'form': form, 'productos': productos, 'active_view': 'vista_productos'})

@login_required(login_url='/logeo/')
def producto_editar(request, id_producto):
    producto = Products.objects.get(id=id_producto)
    
    if(request.method == 'GET'):
        form = ProductoForm(instance=producto)
        return render(request, './app/producto_editar.html', {"form": form, 'producto': producto, 'active_view': 'vista_productos'})
        

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)

        if form.is_valid:
            form.save()
            messages.success(request,'el Producto se ha editado exitosamente.')
            return render(request, "./app/producto_editar.html", {'active_view': 'vista_productos'})
        
        else:
            messages.success(request,'Hubo un erro al intentar editar el Producto.')
            return render(request, "./app/producto.html", {'active_view': 'vista_productos'})

@login_required(login_url='/logeo/')
def producto_eliminar(request, id_producto):

    if(request.method == 'GET'):
        producto = Products.objects.get(id=id_producto)
        producto.delete()
        messages.success(request,'el Producto se ha eliminado exitosamente.')
        return render(request, './app/producto_eliminar.html', {'active_view': 'vista_productos'})
    else:
        messages.success(request,'Hubo un erro al intentar borrar el Producto.')
        return render(request, './app/producto_eliminar.html', {'active_view': 'vista_productos'})

@login_required(login_url='/logeo/')
def seller(request):

    request.method == 'GET'
    vendedores = Sellers.objects.all()

    if request.method =='POST':
        form = SellerForm(request.POST)

        if form.is_valid:
            form.save()
            messages.success(request, 'El vendedor se ha creado con éxito.')
            form = SellerForm()
            return render(request, "./app/vendedor.html", {"form": form, "vendedores": vendedores, 'active_view': 'vista_vendedores'})
    else:
        form = SellerForm()
    return render(request, "./app/vendedor.html", {"form": form, "vendedores": vendedores, 'active_view': 'vista_vendedores'})

@login_required(login_url='/logeo/')
def vendedor_editar(request, id_vendedor):
    vendedor = Sellers.objects.get(id=id_vendedor)
    
    if(request.method == 'GET'):
        form = SellerForm(instance=vendedor)
        return render(request, './app/vendedor_editar.html', {"form": form, 'vendedor': vendedor, 'active_view': 'vista_vendedores'})
        

    if request.method == 'POST':
        form = SellerForm(request.POST, instance=vendedor)

        if form.is_valid:
            form.save()
            messages.success(request,'el Vendedor se ha editado exitosamente.')
            return render(request, "./app/vendedor_editar.html", {'active_view': 'vista_vendedores'})
        
        else:
            messages.success(request,'Hubo un erro al intentar editar el Vendedor.')
            return render(request, "./app/vendedor.html", {'active_view': 'vista_vendedores'})

@login_required(login_url='/logeo/')
def vendedor_eliminar(request, id_vendedor):

    if(request.method == 'GET'):
        vendedor = Sellers.objects.get(id=id_vendedor)
        vendedor.delete()
        messages.success(request,'el Vendedor se ha eliminado exitosamente.')
        return render(request, './app/vendedor_eliminar.html', {'active_view': 'vista_vendedores'})
    else:
        messages.success(request,'Hubo un erro al intentar borrar al Vendedor.')
        return render(request, './app/vendedor_eliminar.html', {'active_view': 'vista_vendedores'})

@login_required(login_url='/logeo/')
def buscar(request):

    q = request.GET.get('q', '')
    productos = Products.objects.filter(name__icontains=q)
 
    if productos:
        return render(request, './app/busqueda.html', {'productos': productos, 'active_view': 'vista_busqueda'})
    else:
        mensaje = 'Producto no encontrado'
        return render(request, './app/busqueda.html', {'mensaje': mensaje, 'active_view': 'vista_busqueda'})

@login_required(login_url='/logeo/')
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) 
            if miFormulario.is_valid():
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "./app/agregarAvatar.html", {'active_view': 'vista_login'})
      else: 
            miFormulario= AvatarFormulario()
      return render(request, "./app/agregarAvatar.html", {"miFormulario":miFormulario, 'active_view': 'vista_avatar'})