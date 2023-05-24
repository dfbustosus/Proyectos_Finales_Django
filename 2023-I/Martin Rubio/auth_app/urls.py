from django.urls import path

from . import views

urlpatterns = [
    path('signin/',views.login_request, name='login-page'),
    path('signup/',views.register_request, name='register-page'),
    path('signout/',views.logout_request, name='logout'),
    path('profile/',views.profile, name='profile-page'),
]