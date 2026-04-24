from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from orders.models import Food 
from django.shortcuts import render, get_object_or_404
from .models import Basket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 

def home(request):
    return render(request, 'Login.html')

def HomePage(request): 
    return render(request, "HomePage.html")

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META.get('HTTP_REFERER', 'basket'))

def logout_view(request):
    logout(request)
    return redirect('Login')

def Payment(request):
    return redirect(request,'Payment.html')
                    
def Bake(request): 
    return render(request, "Bake.html")

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'Bake.html', {'food': food})

def Basket_view(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    
    # Получаем товары текущего пользователя
    basket_items = Basket.objects.filter(user=request.user)
    
    # Считаем сумму
    total_price = sum(item.food.Price * item.quantity for item in basket_items)
    
    context = {
        'basket_items': basket_items,
        'total_price': total_price,
    }
    # ОСТАВЛЯЕМ ТОЛЬКО ЭТОТ RETURN
    return render(request, 'Basket.html', context)

def Menu_view(request):
    products = Food.objects.all() 
    return render(request, 'Menu.html', {'food': products})

@login_required
def basket_add(request, food_id):
    food = Food.objects.get(id=food_id)
    baskets = Basket.objects.filter(user=request.user, food=food)

    if not baskets.exists():
        Basket.objects.create(user=request.user, food=food, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return redirect(request.META.get('HTTP_REFERER', 'Menu'))



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