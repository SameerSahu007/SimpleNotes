from django import forms
from django import http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
# Create your views here.


# def login(request):
#     if request.method == 'POST':
#          form = LoginForm(request.POST) 
#          form_data = request.POST
#          username = form_data.get('username')
#          password1 = form_data.get('password1')
#          fname = form_data.get('fname')
#          lname = form.data.get('lname')

#          user = User(username = username, password = password1, fname = fname, lname = lname)
#          user.save()
#          return redirect('/admin')

#         #  print(form.is_valid())
#         #  if form.is_valid():  
#         #     form.save() 
#         #     return HttpResponse('Valid Credentials')
            

#     form = LoginForm()
#     context = {  
#                 'form':form  
#               }  
#     return render(request, 'notes/login.html', context)

def index(request):
    return render(request, 'notes/main.html')

def testpage(request):
    return HttpResponse("You Made it!!!!!!!! :)")