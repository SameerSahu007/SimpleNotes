from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('testpage', views.testpage),
    path('login/', views.login, name='login')
]