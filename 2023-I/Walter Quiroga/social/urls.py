from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path('', views.feed, name='feed'),
	path('profile/', views.profile, name='profile'),
	path('profile/<str:username>/', views.profile, name='profile'),
	path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
	path('post/', views.post, name='post'),
	path('follow/<str:username>/', views.follow, name='follow'),
	path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('profile/updatePost/<str:pk>/', views.updatePost, name='update-post'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete/<str:id>', views.delete_post, name='delete-post'),
    path('about/', views.about, name='about'),
	
] 