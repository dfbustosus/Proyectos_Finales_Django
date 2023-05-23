from django.shortcuts import render , redirect , get_object_or_404
from django.urls import reverse_lazy
from .models import Prodcto , Marca ,Contacto ,Profile
from .forms import ContactoForm , ProductoForm ,MarcaForm , CustomUserCreationForm , ProfileForm , User
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required , permission_required

# Create your views here.
""""
Vistas Home con buscador
"""
def home(request):
    if(request.GET.get('buscar')):
        data = Prodcto.objects.filter(
            Q(nombre__icontains = request.GET.get('buscar')) |
            Q(descripcion__icontains = request.GET.get('buscar'))|
            Q(marca__nombre__icontains = request.GET.get('buscar'))
            ).distinct()
    else:
        data = Prodcto.objects.all()
    return render(request, 'tienda/home.html', {'data': data})

""""
Vistas Contacto

"""
def contacto(request):
    data = {
        'form' : ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Mensaje Guardado Correctamente')
        else:
            data['form'] = formulario
        
    return render(request, 'tienda/contacto.html' , data)

@permission_required('tienda.view_contacto')
def listar_contactos(request):
    mensajes = Contacto.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(mensajes, 4)
        mensajes = paginator.page(page)
    except:
        raise Http404
    
    
    data = {
        'mensajes' : mensajes,
        'paginator' : paginator
    }
    
    return render(request, 'contacto/listar.html', data)

""""
Galeria

"""

def galeria(request):
    return render(request, 'tienda/galeria.html')

""""
Registro

"""

def registro(request):
    data = {
        'form' : CustomUserCreationForm
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Te has Registrado Correctamente')
            #redirigir al home
            return redirect(to='home')
        data['form'] = formulario
            
    return render(request, 'registration/registro.html', data)


""""
Vistas Productos

"""
@permission_required('tienda.add_prodcto')
def agregar_producto(request):
    data = {
        'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Agregado Correcatmente")
        else:
            data['form'] = formulario
    return render(request, 'producto/agregar.html', data)

@permission_required('tienda.view_prodcto')
def listar_productos(request):
    productos = Prodcto.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(productos, 4)
        productos = paginator.page(page)
    except:
        raise Http404
    
    
    data = {
        'productos' : productos,
        'paginator' : paginator
    }
    
    return render(request, 'producto/listar.html', data)

@permission_required('tienda.change_prodcto')
def modificar_producto(request, id):
    
    producto = get_object_or_404(Prodcto, id=id)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado Correcatmente")
            return redirect(to="listar_productos")
        data["form"] = formulario
        
    return render(request, 'producto/modificar.html', data)

@permission_required('tienda.delete_prodcto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Prodcto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correcatmente")
    return redirect(to="listar_productos")

def detalle_producto(request, id):
    producto = get_object_or_404(Prodcto, id=id)
    #print(producto.precio)
    return render(request, 'producto/detalle.html', {'producto': producto})

""""
Vistas Marcas

"""
@permission_required('tienda.add_marca')
def agregar_marca(request):
    data = {
        'form' : MarcaForm()
    }
    
    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Marca Agregada Correcatmente")
        else:
            data['form'] = formulario
    return render(request, 'marca/agregar.html', data)

@permission_required('tienda.view_marca')
def listar_marcas(request):
    marcas = Marca.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(marcas, 4)
        marcas = paginator.page(page)
    except:
        raise Http404
    
    
    data = {
        'marcas' : marcas,
        'paginator' : paginator
    }
    
    return render(request, 'marca/listar.html', data)

@permission_required('tienda.change_prodcto')
def modificar_marca(request, id):
    
    marca = get_object_or_404(Marca, id=id)
    
    data = {
        'form': MarcaForm(instance=marca)
    }
    
    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado Correcatmente")
            return redirect(to="listar_marcas")
        data["form"] = formulario
        
    return render(request, 'marca/modificar.html', data)

@permission_required('tienda.delete_prodcto')
def eliminar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    messages.success(request, "Eliminado Correcatmente")
    return redirect(to="listar_marcas")


""""
Vistas Perfil

"""

from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return Profile.objects.create(user=self.request.user)
    
    
""""
Vistas Sobre mi

"""

def sobremi(request):
    return render(request, 'tienda/sobremi.html')