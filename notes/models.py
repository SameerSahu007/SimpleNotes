from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    fname =  models.CharField(max_length=35)
    lname =  models.CharField(max_length=35)

class Post(models.Model):
    title =  models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title