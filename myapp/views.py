from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def home(request):
    if request.method == 'GET':
        # Handle GET request
        data = {'message': 'This is a GET request'}
        return render(request, './myapp/home.html', data)
    elif request.method == 'POST':
        # Handle POST request
        return HttpResponse('This is a POST request')