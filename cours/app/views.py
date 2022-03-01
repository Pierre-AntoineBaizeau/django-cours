from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def index():
    return render(request, 'app/index.html')