from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Posts
from .forms import PostsForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.messages import get_messages

class CreatePageTest(TestCase):
       
    def test_create_page_with_permission(self):
        
        self.user = User.objects.create_user(username='userprueba', password='password_123')
        self.client = Client()
    
        self.user.user_permissions.add(35) #De acuerdo al DB , Blog.Can_Edit tiene id=35
        self.client.login(username='userprueba', password='password_123')
        
        # Petición POST
        form_data = {'title':'Test Titulo','subtitle':'Test subtitulo',
                     'Message': 'Esto es una prueba',
                     'imageMain': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
                     'dateAdded' : '2023-05-18 04:29:48.571511','dateModified': '2023-05-19 05:46:33.153497'}
        
        Posts.objects.create(title='Test Titulo', subtitle='Test subtitulo',
                              Message='Esto es una prueba', imageMain='tardigrado.webp', user=self.user)
        
        #Simulación del Post
        response = self.client.post('/pages/create/', form_data)

        # Verificar que se haya creado correctamente
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/newpage.html')
        
        # Verificar que se haya guardado en la DB
        created_page = Posts.objects.get(title='Test Titulo')
        self.assertEqual(created_page.subtitle, 'Test subtitulo')


    def test_create_page_without_permission(self):

        self.user = User.objects.create_user(username='userprueba', password='password_123')
        self.client = Client()
    
        #self.user.user_permissions.add(35) #De acuerdo al DB , Blog.Can_Edit tiene id=35
        self.client.login(username='userprueba', password='password_123')
        
        # Simular una petición POST sin el permiso necesario
        form_data = {'title':'Test Titulo','subtitle':'Test subtitulo',
                     'Message': 'Esto es una prueba','imageMain':'<InMemoryUploadedFile: tardigrado.webp (image/webp)>',
                     'dateAdded' : '2023-05-18 04:29:48.571511','dateModified': '2023-05-19 05:46:33.153497'}
        
        response = self.client.post('/pages/create/', form_data)
        
        # Verificar que la redirección y el mensaje de error se hayan realizado correctamente
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/pages/')
        
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'No tienes permisos para realizar esta operación')

        # Verificar que no se haya creado ningún objeto de página en la base de datos
        self.assertRaises(Posts.DoesNotExist, Posts.objects.get, title='Test Titulo')
