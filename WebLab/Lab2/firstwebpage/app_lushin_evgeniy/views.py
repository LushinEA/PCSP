from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'templates/index.html', {})

def new_home(request):
    return render(request, 'templates/static_handler.html', {})

def hello(request):
    return HttpResponse(u'Hello, World!')

# Create your views here.

