from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import date
# Create your views here.

postagens = [
      {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Alisson Davis",
        "date": date(2021, 1, 7),
        "title":"Moutain Hiking",
        "excerpt" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum incidunt quibusdam repellendus numquam nemo asperiores modi quis magnam, ratione amet quia consequatur praesentium reiciendis id rerum possimus tenetur, distinctio inventore?",
        "content" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum incidunt quibusdam repellendus numquam nemo asperiores modi quis magnam, ratione amet quia consequatur praesentium reiciendis id rerum possimus tenetur, distinctio inventore?",
    },
     {
        "slug":"hike-in-the-air",
        "image":"woods.jpg",
        "author":"Alisson Davis",
        "date": date(2021, 1, 7),
        "title":"Moutain Hiking",
        "excerpt" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum incidunt quibusdam repellendus numquam nemo asperiores modi quis magnam, ratione amet quia consequatur praesentium reiciendis id rerum possimus tenetur, distinctio inventore?",
        "content" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum incidunt quibusdam repellendus numquam nemo asperiores modi quis magnam, ratione amet quia consequatur praesentium reiciendis id rerum possimus tenetur, distinctio inventore?",
    }
]

def get_date(post):
    return post.get("date")

def index(request):
    
    postagens.sort(key=get_date)
    ultimos_posts = postagens[-3:]
    return render(request,"blog/index.html",{
        "posts":ultimos_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "posts": postagens
    })   

def post_detail(request, slug):
    post =  [retorno for retorno in postagens if retorno["slug"] == slug]
   
    return render(request, "blog/post-detail.html",{
        "post" : post[0]
    })