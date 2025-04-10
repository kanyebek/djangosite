from django.shortcuts import render,HttpResponse
import random
from posts.models import Post
# Create your views here.

def test_view(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def html_view(request):
    return render(request, 'base.html')

def site_view(request):
    return render(request, 'site.html')

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', context = {'posts': posts})