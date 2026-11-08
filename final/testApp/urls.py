from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import * #custom forms

urlpatterns = [
    path("", views.home, name = "home"),    
    path("feed/", views.feed, name = "feed"),
    path("profile/", views.profile, name = "profile_page"),
    path("events/", views.events, name = "event_page"),
    #path("clubs/", views.clubs, name = "club_search")
    path("login/", auth_views.LoginView.as_view(template_name="testApp/home.html", authentication_form = CustomLoginForm), name = "login"),
    path("logout/", auth_views.LogoutView.as_view(), name = "logout"),
    path("register/",views.register, name = "register"),
    path("password-reset/",auth_views.PasswordResetView.as_view(
        template_name="testApp/password_reset.html",
        email_template_name="testApp/password_reset_email.html",
        success_url="/password-reset/done/"),
        name="password_reset"),

    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(
        template_name="testApp/password_reset_done.html"),
        name="password_reset_done"),

    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(
        template_name="testApp/password_reset_confirm.html",
        success_url="/password-reset-complete/"),name="password_reset_confirm"),
        
    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(
        template_name="testApp/password_reset_complete.html"),
        name="password_reset_complete"),
]