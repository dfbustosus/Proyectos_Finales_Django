from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from PIL import Image

from Blogregistro.views import obtener_avatar
from Blogapp.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio (request):
    if request.user.is_authenticated:
        return render(request, 'Blogapp/inicio.html', {'avatar': obtener_avatar(request)})
    else:
        return render(request, 'Blogapp/inicio.html')


#  Views de posteos


def posteos (request):
    if request.user.is_authenticated:
        return render(request, 'Blogapp/posteos.html', {'avatar': obtener_avatar(request)})
    else:
        return render(request, 'Blogapp/posteos.html')    

def lista_posteos (request):
    if request.user.is_authenticated:
        posteos = Post.objects.all()
        if len(posteos) != 0:
            return render(request, 'Blogapp/lista_posteos.html', {'posteos': posteos, 'avatar': obtener_avatar(request)})
        else:
            return render(request, 'Blogapp/lista_posteos.html', {'mensaje': 'Todavía no hay posteos. Crea uno!', 'avatar': obtener_avatar(request)})
    else:
        posteos = Post.objects.all()
        if len(posteos) != 0:
            return render(request, 'Blogapp/lista_posteos.html', {'posteos': posteos})
        else:
            return render(request, 'Blogapp/lista_posteos.html', {'mensaje': 'Todavía no hay posteos. Crea uno!'}) 

@login_required
def postFormulario(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.cleaned_data
            titulo = info['titulo']
            subtitulo = info['subtitulo']
            cuerpo = info['cuerpo']
            autor = info['autor']
            fecha = info['fecha']
            imagen = request.FILES['imagen']
            post = Post(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            post.save()
            
            return render(request, 'Blogapp/mostrarPost.html', {'post': post, 'avatar': obtener_avatar(request)})
        else:
            return render(request, 'Blogapp/postFormulario.html', {'form': form, 'avatar': obtener_avatar(request)})
    else:
        form = PostForm()
        return render(request, 'Blogapp/postFormulario.html', {'form': form, 'avatar': obtener_avatar(request)})


def mostrarPost(request, id):
    post = Post.objects.get(id=id)
    if request.user.is_authenticated:
        return render(request, 'Blogapp/mostrarPost.html', {'post': post, 'avatar': obtener_avatar(request)})
    else:
        return render(request, 'Blogapp/mostrarPost.html', {'post': post})


@login_required
def borrar_post(request, id):
    post = Post.objects.get(id=id)
    if request.user.is_superuser:
        post.delete()
        return render(request, 'Blogapp/borrar_post.html', {'mensaje': 'Post borrado exitosamente', 'avatar': obtener_avatar(request)})
    else:
        return render(request, 'Blogapp/borrar_post.html', {'mensaje': 'No tenés permisos para borrar este post', 'avatar': obtener_avatar(request)})
@login_required
def editar_post (request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            post.titulo = info["titulo"]
            post.subtitulo = info['subtitulo']
            post.cuerpo = info['cuerpo']
            post.autor = info['autor']
            post.fecha = info['fecha']
            post.imagen = info['imagen']
            post.save()
            posteos = Post.objects.all()
            return render(request, 'Blogapp/lista_posteos.html', {'mensaje': 'Post editado exitosamente', 'posteos': posteos, 'avatar': obtener_avatar(request)})        
    else:
        form = PostForm(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo, 'cuerpo': post.cuerpo, 'autor': post.autor, 'fecha': post.fecha, 'imagen': post.imagen})
        return render(request, 'Blogapp/editar_post.html', {'form': form, 'post': post, 'avatar': obtener_avatar(request)})


def about (request):
    if request.user.is_authenticated:
        return render(request, 'Blogapp/about.html', {'avatar': obtener_avatar(request)})
    else:
        return render(request, 'Blogapp/about.html')