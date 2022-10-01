from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Post
from django.contrib.auth import logout
# Create your views here.


@login_required
def mynotes(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.user = request.user
        temp.save()
        return redirect('/')

    current_user = User.objects.get(username=request.user.username)
    allposts = Post.objects.filter(user=current_user)

    return render(request, 'notes/mynotes.html',
                  {
                      "form": form,
                      "posts": list(allposts)
                  }
                  )


def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account Created for {username}')
        return redirect('login')

    return render(request, 'notes/signup.html', {'form': form})


@login_required
def delete(request, id):
    current_user = User.objects.get(username=request.user.username)
    Post.objects.filter(user=current_user, id=id).delete()
    return redirect('/')


# def logout_view(request):
#     logout(request)
#     return redirect('login')
