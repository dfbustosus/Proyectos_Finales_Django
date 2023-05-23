from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null= True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"



 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega los campos adicionales que necesites
    description = models.TextField(blank=True)
    webpage = models.URLField(blank=True)

    # Puedes agregar más campos según tus necesidades

    def __str__(self):
        return self.user.username
    



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

models.signals.post_save.connect(create_user_profile, sender=User)