from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    return render(request, 'common/common.html')

def logout_page(request):
    logout(request)
    return redirect('common:index')