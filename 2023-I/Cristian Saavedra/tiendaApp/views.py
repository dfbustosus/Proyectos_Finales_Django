from django.shortcuts import render,get_object_or_404,redirect
from .models import Category, Products,Contact
from .forms import ProductoForm,CategoryForm,ContactoForm,UserRegisterForm
from django.contrib import messages
from django.views.generic import ListView,UpdateView
from django.db.models import Q,Count
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


#Login

def logeo(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                #return render(request, "admin_templates/home.html", {"mensaje":f"Bienvenido {usuario}"})
                messages.success(request, f'Has iniciado sesión {usuario}')
                return redirect(to='home')
            else:
                #messages.error(request, f'Ha habido un error')
                return render(request, "login.html", {"mensaje":"Datos incorrectos"})           
        else:
            messages.error(request, f'Ha habido un error')
            return render(request, "login.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    #messages.error(request, f'Ha habido un error')
    return render(request, 'login.html', {"form": form})

# Vista para registro
login_required(login_url='/')
def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
                username = form.cleaned_data['username']
                form.save()
                messages.success(request, 'Usuario creado')
                return redirect(to='login')
        messages.error(request, 'Ha ocurrido un error') 
    else:
        #form = UserCreationForm()       
        form = UserRegisterForm()  
          
    return render(request,"register.html" ,  {"form":form})



#home dashboard

login_required(login_url='/')
def home(request):

    productos=Products.objects.count()

    categorias=Category.objects.count()
    
    users=User.objects.count()

    #lista de categorias
    prueba=Category.objects.all()
    lir=[]
    ids=[]
    for it in prueba.iterator():
        lir.append(it.nombre)
        ids.append(it.id)
    print(lir)
    #productos por categoria
    cant=[]    
    for c in ids:
        datos=Products.objects.filter(categoria=c).count()
        cant.append(datos)

    print(cant)
    print('-------------')
    print(ids)
    

    data={'productos':productos,'categorias':categorias,'etiquetas':lir,'cant_pxcat':cant,'usuarios':users}
    return render(request, 'admin_templates/home.html', data)


#Categorías
login_required(login_url='/')
def agregar_categoria(request):
    data={

        'form': CategoryForm()
    }
    if request.method == 'POST':
        formulario=CategoryForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Categoría registrado')
        else:
            data['form']=formulario
    return render(request, 'admin_templates/category_create.html', data)

# def listar_categorias(request):
#     categorias=Category.objects.all()
#     data={
#         'categorias':categorias
#     }
#     return render(request, 'admin_templates/categories_list.html', data)

login_required(login_url='/')
class CategoriesListView(ListView):
    model=Category
    template_name='admin_templates/categories_list.html'
    paginate_by=10

    def get_queryset(self):
        filter_val=self.request.GET.get('filter', '')
        order_by=self.request.GET.get('orderby', 'id')
        if filter_val != '':
            cat=Category.objects.filter(Q(nombre__contains=filter_val)).order_by(order_by)
        else:
            cat=Category.objects.all().order_by(order_by)
        return cat

    def get_context_data(self, **kwargs):
        context=super(CategoriesListView, self).get_context_data(**kwargs)
        context['filter']=self.request.GET.get('filter', '')
        context['order_by']=self.request.GET.get('order_by', '')
        context['all_table_fields']=Category._meta.get_fields()
        return context
    

login_required(login_url='/')
def modificar_categoria(request, id):
    producto=get_object_or_404(Category, id=id)
    data={

        'form': CategoryForm(instance=producto)
    }
    if request.method == 'POST':
        formulario=CategoryForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Categoría Modifiada Correctamente')
            return redirect(to='category_list')
        else:
            data['form']=formulario

    return render(request, 'admin_templates/category_update.html', data)


login_required(login_url='/')
def eliminar_categoria(request, id):
    producto=get_object_or_404(Category, id=id)
    producto.delete()
    messages.success(request, 'Categoría Eliminada Correctamente')
    return redirect(to='category_list')


#Productos
login_required(login_url='/')
def agregar_producto(request):
    data={

        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario=ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto registrado')
        else:
            data['form']=formulario
    return render(request, 'admin_templates/product_create.html', data)


class ProductsListView(ListView): #se puede iterar en el template como products_list  es decir nombre de la vista sin ListView más _list
    model=Products
    template_name='admin_templates/product_list.html'


login_required(login_url='/')
def modificar_producto(request, id):
    producto=get_object_or_404(Products, id=id)
    data={

        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario=ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto Modifiado Correctamente')
            return redirect(to='product_list')
        else:
            data['form']=formulario

    return render(request, 'admin_templates/product_update.html', data)

login_required(login_url='/')
def eliminar_producto(request, id):
    producto=get_object_or_404(Products, id=id)
    producto.delete()
    messages.success(request, 'Producto Eliminado')
    return redirect(to='product_list')

# formulario de contacto
def agregar_mensaje_contacto(request):
    data={

        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Mensaje enviado correctamente!')
        else:
            data['form']=formulario
    return render(request, 'admin_templates/form_contacto_create.html', data)


login_required(login_url='/')
class ContactoListView(ListView): #se puede iterar en el template como products_list  es decir nombre de la vista sin ListView más _list
    model=Contact
    template_name='admin_templates/contact_list.html'
    paginate_by=10

    def get_queryset(self):
        filter_val=self.request.GET.get('filter', '')
        order_by=self.request.GET.get('orderby', 'id')
        if filter_val != '':
            cat=Contact.objects.filter(Q(nombre__contains=filter_val)).order_by(order_by)
        else:
            cat=Contact.objects.all().order_by(order_by)
        return cat

    def get_context_data(self, **kwargs):
        context=super(ContactoListView, self).get_context_data(**kwargs)
        context['filter']=self.request.GET.get('filter', '')
        context['order_by']=self.request.GET.get('order_by', '')
        context['all_table_fields']=Contact._meta.get_fields()
        return context