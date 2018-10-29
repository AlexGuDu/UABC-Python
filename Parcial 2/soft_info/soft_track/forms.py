from django import forms
from .models import SwPackage, Dept


class RawSwForm(forms.Form):
    categories = [
        (None, 'Choose a Department')
    ]

    for dept in Dept.objects.all():
        categories.append((dept.name, dept.name))

    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    dept = forms.ChoiceField(widget=forms.Select(
        attrs={
            "class": "browser-default",
        }
    ), choices=categories)

class RawDeptForm(forms.Form):
    name = forms.CharField(max_length=50)
