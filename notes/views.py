import imp
from django.shortcuts import redirect, render
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

@login_required
def mynotes(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.user =  request.user
            form.save()
            return redirect('/')
            
    form = PostForm()
    return render(request, 'notes/mynotes.html', {"form": form})

def signup(request):
    if request.method == 'POST':
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username =  form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('login')
    else:
        form  = UserCreationForm()
    return render(request, 'notes/signup.html' , {'form': form})