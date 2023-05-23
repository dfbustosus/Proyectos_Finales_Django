from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title

class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return "Acerca de mí"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.user.username