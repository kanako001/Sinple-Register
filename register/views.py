from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return render(request, 'views/register/register.html ', {})

def login(request):
    return render(request, 'views/register/login.html ', {})

def outline(request):
    return render(request, 'views/register/list.html', {})