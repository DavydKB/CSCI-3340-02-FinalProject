from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.forms import AuthenticationForm #login/logout 
from django.contrib.auth.decorators import login_required #Need to login to see page.


def home(request):
    if request.user.is_authenticated:
        return redirect("feed")
    form = AuthenticationForm()
    return render(request, "testApp/home.html", {"form": form})

@login_required
def feed(request):
    posts = Post.objects.order_by("-date_created")
    return render(request, "testApp/feed.html", {"posts": posts})

@login_required
def profile(request):
    return render(request, "testApp/profile.html")

@login_required
def events(request):
    return render(request, "testApp/events.html")

#def club