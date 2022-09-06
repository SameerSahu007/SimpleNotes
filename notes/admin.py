from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "description")

# admin.site.register(Post)



