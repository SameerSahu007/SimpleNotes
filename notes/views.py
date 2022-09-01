from django import forms
from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    if request.method == 'POST':
         form = CustomUserCreationForm(request.POST) 
         print(form.is_valid())
         if form.is_valid():  
            form.save() 
            return HttpResponse('Valid Credentials')
            

    form = CustomUserCreationForm()
    context = {  
                'form':form  
              }  
    return render(request, 'notes/login.html', context)

def index(request):
    return render(request, 'notes/main.html')

def testpage(request):
    return HttpResponse("You Made it!!!!!!!! :)")