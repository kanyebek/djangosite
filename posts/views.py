from django.shortcuts import render,HttpResponse
from posts.models import Post
from posts.forms import PostForm
# Create your views here.

def test_view(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def homepage_view(request):
    return render(request, 'base.html')

def site_view(request):
    return render(request, 'site.html')

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', context = {'posts': posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', context = {'post': post})

def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form': form})
        elif form.is_valid():
            tags=form.cleaned_data.pop("tags")
            post = Post.objects.create(**form.cleaned_data)
            post.tags.set(tags)
            return render(request, 'posts/post_detail.html', context={'post': post})
    