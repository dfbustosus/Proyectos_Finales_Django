from django.shortcuts import render, get_object_or_404, redirect
from App1.models import Blog,  About
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from App1.forms import UserProfileForm



def about_view(request):
    about = About.objects.first()
    return render(request, 'about.html', {'about': about})

def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail_view(request, page_id):
    blog = get_object_or_404(Blog, pk=page_id)
    return render(request, 'blog_detail.html', {'blog': blog})

#REGISTRO

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    return render(request, 'login.html')

@login_required
def profile_view(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form})