from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    MODERATOR = (
        ('Moderator', 'Moderator'),
        ('Padrao', 'Padrao'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    profession = models.TextField(max_length=25, blank=True)
    moderator = models.CharField(choices=MODERATOR, max_length=10, default="Padrao")


    def __str__(self):
        return f'{self.user.username} Profile' 

