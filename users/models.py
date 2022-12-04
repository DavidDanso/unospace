from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='uploads/', default='default-avatar.png')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url
        
    def __str__(self):
        return str(self.username)


        

