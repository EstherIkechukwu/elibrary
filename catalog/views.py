from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_books(request):
    return HttpResponse("Hello, world. You're at the books page.")

def greet(request, name):
    return render(request, 'index.html', {'name': name})
