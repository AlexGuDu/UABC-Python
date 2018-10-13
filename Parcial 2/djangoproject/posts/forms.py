from django import forms
from .models import Posts

class FormCreate(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "body"]
