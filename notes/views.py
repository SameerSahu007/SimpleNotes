from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def testpage(request):
    return render(request, 'notes/testpage.html')

def signup(request):
    if request.method == 'POST':
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username =  form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            return redirect('testpage')
    else:
        form  = UserCreationForm()
    return render(request, 'notes/signup.html' , {'form': form})