from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from accounts.forms import UserForm

def login_page(request):
    if request.user.is_authenticated:
        return redirect('http://localhost:8080/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_auth = authenticate(request, username=username, password=password)
        if user_auth:
            login(request, user_auth)
            request['']
            return redirect('http://localhost:8080/')
    return render(request=request, template_name='auth/login.html')


def register_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')