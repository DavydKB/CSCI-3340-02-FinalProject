from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),    
    path("posts/", views.post_list, name = "post_list"),
    path("profile/", views.profile, name = "profile_page"),
    path("events/", views.events, name = "event_page")
    #path("clubs/", views.clubs, name = "club_search")
]