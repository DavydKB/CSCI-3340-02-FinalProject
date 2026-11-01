from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.order_by("-date_created")
    return render(request, "testApp/post_list.html", {"posts": posts})

def home(request):
    return render(request, "testApp/home.html")

def profile(request):
    return render(request, "testApp/profile.html")

def events(request):
    return render(request, "testApp/events.html")

#def club