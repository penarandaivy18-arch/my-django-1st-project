from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def about(request):
    return render(request, 'about.html', {'title': 'About'})
