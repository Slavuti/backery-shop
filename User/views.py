from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from orders.models import Food 
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'Login.html')

def HomePage(request): 
    return render(request, "HomePage.html")

def Bake(request): 
    return render(request, "Bake.html")

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'Bake.html', {'food': food})

def Menu_view(request):
    products = Food.objects.all() 
    return render(request, 'Menu.html', {'food': products})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Login') # Теперь кидает на главную магазина
        else:
            # Если форма невалидна, мы вернем страницу с формой, 
            # которая уже содержит ошибки (form.errors)
            return render(request, 'Register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'Register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() # Это более надежный способ получить юзера
            login(request, user)
            return redirect('HomePage')
    else:
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')