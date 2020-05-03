from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    thumbnail = models.ImageField(upload_to='thumbnail/', blank=True)
    introduction = models.TextField()

    def __str__(self):
        return self.name