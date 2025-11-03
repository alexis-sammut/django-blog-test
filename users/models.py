from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary.utils import cloudinary_url
from django.templatetags.static import static

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        storage=MediaCloudinaryStorage(),
        upload_to='profile_pics/',
        null=True,
        blank=True
    )
    
    def get_image_url(self):
        if self.image: # Generate a Cloudinary thumbnail URL
            return cloudinary_url(
                self.image.name,
                width=300,
                height=300,
                crop='fill',
                gravity= 'face'
            )[0]
        
        else: # fallback to static default image return static('blog/default.jpg')
             return static('blog/default.jpg')
    
    def __str__(self):
        return f'{self.user.username} Profile'