from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PostForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def feed(request):
	posts = Post.objects.all()

	context = { 'posts': posts}
	return render(request, 'social/feed.html', context)

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('feed')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'social/register.html', context)

@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect('feed')
	else:
		form = PostForm()
	return render(request, 'social/post.html', {'form' : form })



def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else:
		posts = current_user.posts.all()
		user = current_user
	return render(request, 'social/profile.html', {'user':user, 'posts':posts})


def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('feed')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('feed')

@login_required
def updatePost(request, pk):
	post = Post.objects.get(id=pk)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post.save()
			messages.success(request, 'Post actualizado')
			return redirect('profile')
	else:
		post.save()
	
	context = {
		"form": form
	}
	return render(request, 'social/edit.html', context)

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            data = form.cleaned_data
            user.profile.image = data.get('Foto') if data.get('Foto') else user.profile.image
            user.save()
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'social/edit_profile.html', {'form': form})

@login_required
def delete_post(request, id):
	data = get_object_or_404(Post, id=id)
	data.delete()
	return redirect('feed')


def about(request):
	return render(request, 'social/about.html', context=None)