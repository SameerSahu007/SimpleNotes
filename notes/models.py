from enum import Flag
from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}, {self.title}, {self.description} "
