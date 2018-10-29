from django import forms
from .models import Paper, PaperCategory

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ["title", "body"]

class RawPaperForm(forms.Form):
    categories = [
        (None, 'Choose a Category')
    ]

    for papercategory in PaperCategory.objects.all():
        categories.append((papercategory.name, papercategory.name))

    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(widget=forms.Select(
        attrs={
            "class": "browser-default",
        }
    ), choices=categories)
    author = forms.CharField(max_length=50)
