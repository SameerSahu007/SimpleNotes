from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.mynotes, name='mynotes'),
    path('mynotes', views.mynotes, name='mynotes'),
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(
        template_name='notes/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='notes/logout.html'), name='logout'),
    path('delete/<int:id>', views.delete, name='delete')
]
