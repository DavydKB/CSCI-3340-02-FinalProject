from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name = "home"),    
    path("feed/", views.feed, name = "feed"),
    path("profile/", views.profile, name = "profile_page"),
    path("events/", views.events, name = "event_page"),
    #path("clubs/", views.clubs, name = "club_search")
    path("login/", auth_views.LoginView.as_view(template_name="testApp/home.html"), name = "login"),
    path("logout/", auth_views.LogoutView.as_view(), name = "logout"),
]