from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.title
      


class Post(models.Model):
    STATUS = (
        ('Mostrar', 'Mostrar'),
        ('Não Mostrar', 'Não mostrar'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    status = models.CharField(choices=STATUS, max_length=15, default="Mostrar")
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='posts_pics', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

