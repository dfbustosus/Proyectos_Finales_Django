from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null = True, blank = True)
    bio = models.TextField(null = True, blank = True)
    link = models.URLField(max_length = 200, null = True, blank = True)
 
    def __str__(self):
        return f" Perfil de usuario de: {self.user.username} ({self.user.first_name} {self.user.last_name})-- (Avatar,Bios,PagWeb)"