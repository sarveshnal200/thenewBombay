from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/blog.html', {'posts': posts})


def home(request):
    return render(request, 'myblog/index.html')


def about(request):
    return render(request,'myblog/about.html')