from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import date

from .models import Post
# Create your views here.

postagens = [
     
]


def index(request):
    ultimos_posts = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{
        "posts":ultimos_posts
    })

def posts(request):
    postagens = Post.objects.all()
    return render(request, "blog/all-posts.html",{
        "posts": postagens
    })   

def post_detail(request, slug):
    post = Post.objects.get(slug = slug)
   
    return render(request, "blog/post-detail.html",{
        "post" : post
    })