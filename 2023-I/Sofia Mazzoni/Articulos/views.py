from django.shortcuts import render
from Articulos.models import Entradas
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def home(request):
	articulos = Entradas.objects.all()
	return render(request,"bienvenida.html",{"articulos":articulos})
	
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm

@login_required
def messages(request):
    inbox = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    outbox = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'messages.html', {'inbox': inbox, 'outbox': outbox})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Message sent.')
            return redirect('messages')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})
