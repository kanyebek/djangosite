from django.shortcuts import render,HttpResponse, redirect
from posts.models import Post
from posts.forms import PostForm, SearchForm, PostForm2
from django.contrib.auth.decorators import login_required

# Create your views here.

def test_view(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def homepage_view(request):
    return render(request, 'base.html')

def site_view(request):
    return render(request, 'site.html')

@login_required(login_url='/login/')
def post_list_view(request):
    limit = 3
    if request.method == 'GET':
        posts = Post.objects.all()
        form = SearchForm()
        search_q = request.GET.get('search_q')
        category_id = request.GET.get('category_id')
        ordering = request.GET.get('ordering')
        page = int(request.GET.get('page', 1))
        if category_id:
            posts = posts.filter(category__id=category_id)
        if search_q:
            posts = posts.filter(title__icontains  = search_q)
        if ordering:
            posts = posts.order_by(ordering)
        
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else: 
            max_pages = round(max_pages)
        start = (page - 1) * limit
        end = page * limit
        posts = posts[start:end]

        return render(request, 'posts/post_list.html', context = {'posts': posts, 'form': form, 'max_pages':range(1, int(max_pages) + 1)})
@login_required(login_url='/login/')
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', context = {'post': post})
@login_required(login_url='/login/')
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
            return redirect('/posts/')
    
@login_required(login_url='/login/')
def post_update_view(request, post_id):
    post = Post.objects.filter(id=post_id, author = request.user).first()
    if not post:
        return redirect('/posts/')
    if request.method == 'GET':
        form = PostForm2(instance=post)
        return render(request, 'posts/post_update.html', context={'form': form})
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, 'posts/post_update.html', context={'form': form})
        elif form.is_valid():
            tags=form.cleaned_data.pop("tags")
            form.save()
            post.tags.set(tags)
            return redirect(f'/posts/{post_id}/')
        
@login_required(login_url='/login/')
def post_delete_view(request, post_id):
    Post.objects.filter(id=post_id, author = request.user).first().delete()
    return redirect('/profile/')
    