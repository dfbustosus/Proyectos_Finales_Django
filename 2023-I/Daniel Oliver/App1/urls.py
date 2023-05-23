from django.urls import path
from App1 import views
from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('about/', views.about_view, name='about'),
    path('pages/', views.blog_list_view, name='blog_list'),
    path('pages/<int:page_id>/', views.blog_detail_view, name='blog_detail'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
]




