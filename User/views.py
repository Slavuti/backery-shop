from django.shortcuts import render
from django.http import HttpResponse

def Login(request): # Функция которая вызывает страницу Login.html
    return render(request,"Login.html")
