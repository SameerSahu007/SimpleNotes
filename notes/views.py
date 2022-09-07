from collections import UserString
from traceback import print_tb
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Post
# Create your views here.


@login_required
def mynotes(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            return redirect('/')

    form = PostForm()
    current_user =  User.objects.get(username = request.user.username)
    allposts =  Post.objects.filter(user = current_user )

    return render(request, 'notes/mynotes.html',
                  {
                      "form": form,
                      "posts": list(allposts)
                  }
                  )


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'notes/signup.html', {'form': form})

@login_required
def delete(request, id):
    print(id)
    current_user =  User.objects.get(username = request.user.username)
    Post.objects.filter(user = current_user, id = id).delete()
    return redirect('/')
