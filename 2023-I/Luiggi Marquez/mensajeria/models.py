from django.db import models
from django.contrib.auth.models import User


class MessagesChat(models.Model): 

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent', default=None) 
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received') 
    message = models.TextField(blank=False, null=False) 
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Chat Between ----> sender: {self.sender}  ----> Receiver: {self.receiver}"
    
