from django.shortcuts import render, redirect
# Usamos notacion de tipos para obtener ayuda del IDE
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserEditForm, CustomAuthenticationForm

TEMPLATES = {  # Utilizamos una constante para mantener en un solo lugar los valores de los templates
    'login': 'auth/login.html',
    'register': 'auth/register.html',
    'profile': 'auth/profile.html',
}
# Create your views here.


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        # Cualquier método HTTP que no sea post (envío del formulario) renderizará la pagina de login
        return render(request, TEMPLATES['login'], {'form': CustomAuthenticationForm()})

    # En este punto podemos estar seguros que el método HTTP es POST
    form = CustomAuthenticationForm(request, data=request.POST)

    if not form.is_valid():
        # Error first, si el form no es valido, mostramos el error
        return render(request, TEMPLATES['login'], {'form': form, 'errors': {'type': 'error', 'value': 'error up'}})

    # En este punto estamos seguros que el form es válido
    # Obtenemos usuario y contraseña
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    # Autenticamos el usuario
    user = authenticate(username=username, password=password)

    if user is None:
        # Error first: si las credenciales están mal, user será None y debemos mostrar el error
        return render(request, TEMPLATES['login'], {'form': form, 'errors': {'type': 'error', 'value': 'error up'}})

    # En este punto el login es correcto
    login(request, user)

    # Utilizando "error first" el código nos queda con menos identaciones y se hace mucho más fácil de leer

    # Utilizamos redirect en vez de render para redirigirnos a otra página (cambia la URL)
    return redirect('home-page')


def register_request(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        # Cualquier método HTTP que no sea post (envío del formulario) renderizará la pagina de registro
        return render(request, TEMPLATES['register'], {'form': CustomUserCreationForm()})

    # En este punto podemos estar seguros que el método HTTP es POST
    form = CustomUserCreationForm(request.POST)

    if not form.is_valid():
        # Error first, si el form no es valido, mostramos el error
        errors = [{'type': k, 'value': v}
                  for k, v in form.error_messages.items()]
        context = {
            'form': form,
            'errors': errors,
        }
        return render(request, TEMPLATES['register'], context)

    # En este punto estamos seguros que el form es válido y podemos guardarlo para terminar el registro
    form.save()
    return redirect('home-page')


def logout_request(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('home-page')


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    current_user = request.user
    if request.method != 'POST':
        # Cualquier método HTTP que no sea post (envío del formulario) renderizará la pagina de perfil
        initial_state = {
            'email': current_user.email,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            # 'description': current_user.description,
            # 'webpage': current_user.webpage,
        }
        return render(request, TEMPLATES['profile'], {'form': CustomUserEditForm(initial=initial_state)})

    # En este punto podemos estar seguros que el método HTTP es POST
    form = CustomUserEditForm(request.POST)

    if not form.is_valid():
        # Error first, si el form no es valido, mostramos el error
        return render(request, TEMPLATES['profile'], {'form': form, 'error': f'Error en el formulario'})

    # En este punto estamos seguros que el form es válido y podemos guardarlo para terminar el perfil
    new_user_data = form.cleaned_data
    current_user.first_name = new_user_data['first_name']
    current_user.last_name = new_user_data['last_name']
    current_user.description = new_user_data['description']
    current_user.webpage = new_user_data['webpage']
    current_user.email = new_user_data['email']

    current_user.save()

    if new_user_data['password1']:
        current_user.password1 = new_user_data['password1']
        current_user.password2 = new_user_data['password2']
        current_user.save()

    return render(request, TEMPLATES['profile'], {'form': form, 'success': f'Cambios guardados correctamente'})

