from django.shortcuts import render
from django.http import HttpResponse


def HomepPage(request): # Функция которая вызывает страницу HomePage.html
    return render(request, "orders/HomePage.html")
def AboutUs(request): # Функция которая вызывает страницу AboutUs
    return render(request, "orders/AboutUs.html")

def Basket(request): # Функция которая вызывает страницу Корзина/Basket
    return render(request, "orders/Basket.html")

# ПОКА НЕ ИСПОЛЬЗУЕТЬСЯ def NoName(request): # Функция которая вызывает страницу x Продукта 
    return render(request,"Basket.html")

