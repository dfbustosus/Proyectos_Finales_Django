from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import MessagesChat

class SendMessageTest(TestCase):

       
    def test_send_message(self):

        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='testpassword_1')
        self.user2 = User.objects.create_user(username='user2', password='testpassword_2')

        # Iniciar sesión como user1
        self.client.login(username='user1', password='testpassword_1')

        # Simular POST 
        postSimulado = {'message': 'mensaje de prueba','receiver': self.user2.pk}
        response = self.client.post('/mensajeria/chatRoom/receive'.format(self.user2.pk), postSimulado)

        # Verificar  redirección a la vista del chat y el código de respuesta
        self.assertRedirects(response, reverse('chatroom-getmsgs', kwargs={'id': self.user2.pk}))
        self.assertEqual(response.status_code, 302)

        # Aqui se chequea si se creo el mensaje en la DB
        messages = MessagesChat.objects.filter(sender=self.user1, receiver=self.user2, message='mensaje de prueba')
        self.assertEqual(messages.count(), 1)

    def test_invalid_request_method(self):

        self.client = Client()
        self.user1 = User.objects.create_user(username='user1', password='testpassword_1')
        self.user2 = User.objects.create_user(username='user2', password='testpassword_2')

        # Iniciar sesión como user1
        self.client.login(username='user1', password='testpassword_1')

        # Simular una petición GET en lugar de una petición POST
        response = self.client.get(reverse('chatroom-sendmsgs'))
        
        # Verificar que se reciba una respuesta de "Invalid request method."
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), 'Invalid request method.')
