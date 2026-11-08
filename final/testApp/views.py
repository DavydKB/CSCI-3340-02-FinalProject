from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required #Need to login to see page.
from .forms import CustomLoginForm, CustomRegisterForm

def home(request):
    if request.user.is_authenticated:
        return redirect("feed")
    form = CustomLoginForm()
    return render(request, "testApp/home.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('feed')
    else:
        form = CustomRegisterForm()
        
    return render(request, "testApp/register.html", {"form": form})

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