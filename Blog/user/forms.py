from django.contrib.auth.forms import UserCreationForm
from .models import User,Addinfo
from django import forms


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class addForm(forms.ModelForm):
    class Meta:
        model = Addinfo
        fields = ("nickname",)