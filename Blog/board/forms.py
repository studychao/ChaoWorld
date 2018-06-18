from django import forms
from .models import usercomment

class commentform(forms.ModelForm):
    class Meta:
        model = usercomment
        fields = ['name','email','text']
