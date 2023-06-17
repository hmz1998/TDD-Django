from django.shortcuts import render

from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {"posts": posts})


def post_detail(request, slug):
    return render(request, "posts/detail.html")