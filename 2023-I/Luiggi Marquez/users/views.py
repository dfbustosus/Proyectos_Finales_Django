from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.models import User, Permission
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Profile
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import editUserForm
from django.utils.decorators import method_decorator
from django.contrib import messages

@login_required
def base(request):
    hero = True
    return render(request, 'index.html',{
            'hero': hero, 'about':True
    })


def signup(request):

    if(request.user.is_authenticated):
        return redirect('home')
    else:

        if (request.method == 'GET'):
            return render(request, "signUp.html",{
            'form': UserRegisterForm
            })
        else:

            if(request.POST['password1'] == request.POST['password2']):
                try:
                    form = UserRegisterForm(request.POST)
                    if form.is_valid():
                        form.clean_email()
                        info = form.cleaned_data
                        user = User.objects.create_user(username=str(info['username']).lower(), password=str(info['password1']), first_name=str(info['first_name']), last_name=str(info['last_name']), email=str(info['email']))
                        user.save()
                        user.user_permissions.add(Permission.objects.get(codename='can_view'))
                        login(request, user)
                        profile= Profile.objects.create(user=user, bio='', avatar='', link ='')
                        profile.save()
                        return redirect('home')
                    else:
                        print(form.errors)
                        return render(request, "signUp.html",{
                        'form': UserRegisterForm, 'errors':form.errors
                    })
                except:
                    return render(request, "signUp.html",{
                    'form': UserRegisterForm, 'errors':'Usuario ya Existe'
                    })

            else:
                return render(request, "signUp.html",{
                'form': UserRegisterForm, 'errors':'Password no coinciden'
                })

@login_required         
def log_out(request):
    logout(request)
    return redirect('home')

@never_cache
def log_in(request):

    if(request.user.is_authenticated):
        return redirect('home')
    else:
        if(request.method == 'GET'):

            return render(request, "login.html",{
                'form': AuthenticationForm
            })
        else:

            user = authenticate(request,username=request.POST['username'].lower(), password=request.POST['password'])

            if(user is None):
                return render(request, "login.html",{
                'form': AuthenticationForm, 'errors':"Usuario/Password erróneo"
            })
            else:
                login(request, user)
                return redirect('home')

@login_required 
def profile(request):
   return render(request, "profile.html")           

@login_required           
def edituser(request):
    user = request.user

    if (request.method == 'GET'):
            return render(request, "edituser.html",{
            'form': editUserForm(user=request.user)
            })
    else:
        
        form = editUserForm(request.POST,user=request.user)

        if form.is_valid():
            info = form.cleaned_data
            form.clean_email()
            user.email = info['email']
            user.first_name = info['first_name']
            user.last_name = info['last_name']

            if(((info['password1'] != '') and (info['password2'] != ''))) : user.set_password(info['password1'])
            if(info['password1'] != info['password2'] ):
                return render(request,"edituser.html", {
                'form': editUserForm(user=request.user), 'errors':'No puede quedar en blanco ningún campo de Password'
                })

            user.save()
            login(request, user)
            return redirect('profile')
        
        return render(request,"edituser.html", {
            'form': editUserForm(user=request.user), 'errors':form.errors
        })
         
             
@method_decorator(login_required, name='dispatch')     
class editprofile(UpdateView):
   
    template_name = 'editprofile.html'
    model = Profile
    fields = [ 'avatar', 'bio', 'link']
    success_url = reverse_lazy('editprofile')

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user = self.request.user)
        return profile

@login_required
def deleteuser(request, id):
     
    
    if (request.user.has_perm('blog.can_delete')):
        deleteUser = User.objects.get(id=id)
        deleteUser.delete()
    else:
        messages.error(request, 'No tienes permisos para realizar esta operación')

    return redirect('Profiles')

@login_required
def profileIndividual(request, id):

    profile = User.objects.get(id = id)
    return render(request, 'profileIndividual.html',{ 'profile':profile} )

@login_required
def about(request):
    return render(request,'about.html')