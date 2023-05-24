from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog
from .forms import BlogForm

from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/home.html', {'blogs': blogs})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

def about(request):
    return render(request, 'blogs/about.html')

@login_required
def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog-detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blogs/blog_update.html', {'form': form})

@login_required
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog-detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogs/blog_update.html', {'form': form})

from django.core.files.storage import default_storage

@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    # Eliminar la imagen asociada al blog
    if blog.image:
        default_storage.delete(blog.image.path)

    # Eliminar el objeto Blog
    blog.delete()
    return redirect('blog-page')


class Error404View(TemplateView):
    template_name = "error/404.html"