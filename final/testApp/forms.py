from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import Post


User = get_user_model()

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = "Username or Email",
        widget = forms.TextInput(attrs={
            "placeholder": "Username or Email",
            "class": "form-control"
        }),
        max_length=20,
    )

    def clean(self):
        username_or_email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username_or_email and password:
            user = User.objects.filter(
                email__iexact=username_or_email
            ).first()

            if user:
                username_or_email = user.get_username()

            self.user_cache = authenticate(
                self.request,
                username=username_or_email,
                password=password
            )

            if self.user_cache is None:
                raise self.get_invalid_login_error()

            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "placeholder": "Username or Email",
            "class": "form-control"
        })

        self.fields["password"].widget.attrs.update({
            "placeholder": "Password",
            "class": "form-control"
        })

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    username = forms.CharField(
        max_length = 20,
        required = True
    )
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self): #sees if email is already used
        email = self.cleaned_data["email"]

        if User.objects.filter(email__iexact = email).exists():
            raise forms.ValidationError("This email is already registered.")

        return email


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]