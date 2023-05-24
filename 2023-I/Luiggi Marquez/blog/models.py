from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Posts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 100)
    Message = RichTextField(blank=False, null=False, default='')
    imageMain = models.ImageField(upload_to='blogs',  null = True, blank = True)
    dateAdded = models.DateTimeField(auto_now_add = True)
    dateModified = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f" Post: {self.title} --- By: {self.user.first_name} {self.user.last_name}"
   
    
    class Meta:
        verbose_name_plural ='Posts'
        ordering = ['-dateModified']
        permissions = (
            ("can_view", "Can view Posts"),
            ("can_edit", "Can edit Posts"),
            ("can_delete", "Can delete Posts"),
        )
 