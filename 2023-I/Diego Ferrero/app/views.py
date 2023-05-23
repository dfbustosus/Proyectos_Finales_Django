from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# las vistas...

def home(request):
    post = Blog.objects.all()
    return render(request, 'home.html', {'posts':post})

def acercaDe(request):
    return render(request,'acerca.html',{})

def agregarPost(request):

    if request.method == 'GET':
        form = BlogForm()
        return render(request, 'agregarPost.html', {
            'formulario': form
        })
    
    elif request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            pic = form.save(commit=False)
            pic.owner = request.user
            pic.save()
            form.save_m2m()
            return redirect('/')
        else:
            return HttpResponse("Error")
    return redirect ('/')

def verPost(request,id):
    post = Blog.objects.get(id=id)
    return render (request,'resultado_busqueda.html',{'post':post})

def stream_file(request, id):
    ad = get_object_or_404(Blog, id=id)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response

def eliminarPost(request,id):
    post = Blog.objects.get(id=id)
    post.delete()
    return redirect('/')

def editarPost(request, id):
    if request.method == 'GET':
        ad = get_object_or_404(Blog, id=id)
        form = BlogForm(instance=ad)
        ctx = {'formulario': form}
        return render(request, 'agregarPost.html', ctx)

    if request.method == 'POST':
        ad = get_object_or_404(Blog, id=id)
        form = BlogForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid():
            ctx = {'formulario': form}
            return render(request, 'agregarPost.html', ctx)

        pic = form.save(commit=False)
        pic.owner = request.user  # Asignar el atributo owner
        pic.save()
        form.save_m2m()
        return redirect('/')

from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


