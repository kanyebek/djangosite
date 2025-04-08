from django.shortcuts import render,HttpResponse
import random

# Create your views here.

def test_view(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def html_view(request):
    return render(request, 'base.html')
