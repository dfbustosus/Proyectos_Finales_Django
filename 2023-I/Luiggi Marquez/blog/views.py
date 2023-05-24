from django.shortcuts import render, redirect
from .forms import PostsForm, PostsEditForm
from .models import Posts
from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse

@login_required
def createPage(request):


    if(request.user.has_perm('blog.can_edit') or request.user.has_perm('blog.can_delete') ):

        if(request.method == "POST"):
            
            form = PostsForm(request.POST,request.FILES)
            print(form)
            if(form.is_valid()):

                info = form.cleaned_data
                print(info)
                usertable= User.objects.get(username=request.user.username)
                image = request.FILES['imageMain']
            
                blog = Posts.objects.create(user=usertable, title = info['title'], subtitle=info['subtitle'], imageMain = image, Message = info['Message'])
                blog.save()

                return redirect('pages')
            else:
                return render(request, 'blog/newpage.html',{
                'form': PostsForm, 'errors':form.errors})

    
        return render(request, 'blog/newpage.html',{
            'form': PostsForm
        })
    
    else:

        messages.error(request, 'No tienes permisos para realizar esta operación')
        return redirect('pages')


@login_required
def pagesListView(request):

    canDelete=False
    pagesList=Posts.objects.all()
    if (request.user.has_perm('blog.can_delete')):
        canDelete=True   
    return render(request,'blog/pages.html',{
        'pages': pagesList, 'canDelete':canDelete
    })


@login_required
def pageDetailView(request,id):

    post = Posts.objects.filter(id=id)
    return render(request,'blog/pageDetails.html',{
        'post' : post
    })


@login_required
def pageEdit(request,id):

    user=request.user
    posts = Posts.objects.get(id=id)
   
    if (user.has_perm('blog.can_edit') or user.has_perm('blog.can_delete')):
        
        if (request.method == 'GET'):
                return render(request, "blog/pageEdit.html",{
                'form': PostsEditForm(instance=posts), 'id':id
                })
    
        else:
            
            form = PostsEditForm(request.POST,request.FILES, instance=posts)
            imageActual=Posts.objects.get(id=id).imageMain

            if form.is_valid():
                
                post_instance = form.save(commit=False)
                if(user.has_perm('blog.can_delete')):
                    if form.cleaned_data.get('delete_image'):
                        if (post_instance.imageMain):
                            post_instance.imageMain.delete()
                            post_instance.imageMain = None

                elif(user.has_perm('blog.can_edit') and (form.cleaned_data['imageMain'] != imageActual) ):
                    messages.error(request, 'Access Denied - No tienes permisos para cambiar la imagen')
                    return render(request,'blog/pageEdit.html',{'form': PostsEditForm(instance=posts), 'id':id})

                # Guardar los cambios en la publicación
                post_instance.save()
    

        url = reverse('details', args=[id])
        return redirect(url)
    
    else:
        messages.error(request, 'No tienes permisos para realizar esta operación')
        return redirect('details', id)

@login_required
def deletePage(request,id):

    user = request.user
    if(user.has_perm('blog.can_delete')):

        post = Posts.objects.get(id=id)
        post.delete()
        
    else:
        messages.error(request, 'No tienes permisos para realizar esta operación')
        return redirect('details', id)

    return redirect('pages')

@login_required
def searchPost (request):

    if(request.GET != {}):
        
        canDelete=False
        if (request.user.has_perm('blog.can_delete')):
            canDelete=True 

        empty = False
        consulta = Posts.objects.filter(
            Q(user__last_name__icontains=request.GET['busqueda']) |
            Q(title__icontains=request.GET['busqueda']) |
            Q(subtitle__icontains=request.GET['busqueda']) |
            Q(user__first_name__icontains=request.GET['busqueda']))

        if(len(consulta) == 0):
            empty = True

        return render(request, 'blog/pagesSearch.html', {
            'pages' : consulta, 'empty' : empty, 'canDelete':canDelete
        })
        
    else:
        print('entro a else')
        return render(request,'blog/pagesSearch.html')
    