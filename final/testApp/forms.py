from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = "Username or Email", 
        widget = forms.TextInput(attrs={"placeholder": "Enter username or email"}),
        max_length = 20,
        )

    def clean(self):
        username_or_email = self.cleaned_data.get("username") #retrieve username/password
        password = self.cleaned_data.get("password")
        if username_or_email and password:
            user = User.objects.filter( #search for username/email
                email__iexact=username_or_email
            ).first()

            if user: #get username from provided username/email
                username_or_email = user.get_username()

            self.user_cache = authenticate( #authenticate with given username/email and password
                self.request,
                username = username_or_email,
                password = password
            )

            if self.user_cache is None:
                raise self.get_invalid_login_error()

            self.confirm_login_allowed(self.user_cache) #check if user can login

        return self.cleaned_data


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