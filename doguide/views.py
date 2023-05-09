from django.shortcuts import render

def home(requests):
    return render(request, 'home.html')