from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'common/common.html')

def logout_page(request):
    logout(request)
    return redirect('common:index')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_id = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')
            user = authenticate(username=user_id, password=user_password)
            login(request, user)
            return redirect('common:index')
    else:
        form = UserCreationForm()

    return render(request, 'common/signup.html', {'form': form})