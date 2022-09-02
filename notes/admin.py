from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser, Post

# Register your models here.


admin.site.register(Post)
admin.site.register(CustomUser, UserAdmin)


