from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .forms import *
from .models import *

# Create your views here.

def index(request):
    posts = Post.objects.all()[:3]

    return render(request, 'index.html', {
        'posts':posts,
    })

# ---------- SESIONES ----------#


def signup(request):
    if request.method == 'GET':
        return render(request, 'sesion/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect('posts')
            except IntegrityError:
                return render(request, 'sesion/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'sesion/signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'sesion/signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sesion/signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('posts')


# ---------- POSTS ----------#
@login_required
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {
        'posts': posts
    })

@login_required
def crear_post(request):
    if request.method == 'GET':
        return render(request, 'posts/crear_post.html', {
            'form': CrearPostForm
        })
    else:
        try:
            form = CrearPostForm(request.POST, request.FILES)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.autor = request.user
                new_post.save() 
                return redirect('posts')

            return redirect('posts')
        except ValueError:
            return render(request, 'posts/crear_post.html', {
                'form': CrearPostForm,
                'error': 'Datos Invalidos',
            })

@login_required
def post_detail(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=post_id)
        form = CrearPostForm(instance=post)

        comentarios = Comentario.objects.filter(post_id=post_id)
        imagen = Post.objects.filter(pk=post_id)

        return render(request, 'posts/post_detail.html', {
            'post': post,
            'form': form,
            'comentarios': comentarios,
            'imagen' : imagen[0].imagen.url
        })
    else:
        try:
            post = get_object_or_404(Post, pk=post_id, autor=request.user)
            form = CrearPostForm(request.FILES, request.POST, instance=post)
            if form.is_valid():
                form.save()

            return redirect('posts')
        except ValueError:
            return render(request, 'posts/post_detail.html', {
                'post': post,
                'form': form,
                'error': 'Error al actualizar el post'
            })

@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, autor=request.user)
    # print(post)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')


# ---------- COMENTARIOS ----------#
@login_required
def crear_comentario(request, post_id):
    comentario = Comentario.objects.create(
        nombreUsuario=request.user,
        comentario=request.POST['comentar'],
        post_id=post_id
    )
    comentario.save()
    return redirect('posts')

@login_required
def eliminar_comentario(request, coment_id):
    comentario = get_object_or_404(
        Comentario, id=coment_id, nombreUsuario=request.user)
    if request.method == 'POST':
        comentario.delete()
        return redirect('posts')

# ---------- PERFIL ----------#
@login_required
def avatarPerfil(request):
    user = request.user
    avatares= Avatar.objects.filter(user=request.user.id)
    return render(request, 'perfil/perfil.html', {
        "url":avatares[0].imagen.url,
        'user':user
        })

@login_required
def some_view(request):
    user_avatar = Avatar.objects.get(user = request.user)
    return render(request, 'layouts/base.html', {
        'user_avatar':user_avatar
    })

@login_required
def agregarAvatar(request):
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES)
            if miFormulario.is_valid():
                  u = User.objects.get(username=request.user)
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "index.html")
      else: 
            miFormulario= AvatarFormulario()
      return render(request, "perfil/agregarAvatar.html", {"miFormulario":miFormulario})

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
            return render(request, "index.html")
    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "perfil/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})







def aboutMe(request):
    return render(request, 'about.html')


