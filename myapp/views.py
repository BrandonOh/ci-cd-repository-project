from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == 'GET':
        # Handle GET request
        data = {'message': 'This is a GET request'}
        return render(request, './myapp/home.html', data)
    elif request.method == 'POST':
        # Handle POST request
        return HttpResponse('This is a POST request')