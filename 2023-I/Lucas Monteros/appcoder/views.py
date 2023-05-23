from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from appcoder.models import About, Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from appcoder.forms import UsuarioForm
from appcoder.models import Avatar, Post, Mensaje, About
from django.contrib.auth.admin import User

def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "appcoder/index.html", {"posts": posts})

def about(request):
    return render(request, "appcoder/about.html", {})

class PostDetalle(DetailView):
    model = Post

class PostListar(ListView):
    model = Post  

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("appcoder-listar")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("appcoder-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("appcoder-listar")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('appcoder-listar')

#http://localhost:8000/appcoder/login/?next=/appcoder/listar/
class UserLogin(LoginView):
    next_page = reverse_lazy('appcoder-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('appcoder-listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('appcoder-listar')


class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('appcoder-listar')


class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("appcoder-mensajes-crear")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("appcoder-mensajes-listar")

class AboutListar(ListView):
    model = About
# Create your views here.
