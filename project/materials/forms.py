from django import forms
from .models import Material, Comment


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["title", "material_type", "body", "author"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "material_type": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "body"]

    widgets = {
        "author": forms.TextInput(attrs={"class": "form-control"}),
        "body": forms.Textarea(attrs={"class": "form-control"}),
    }
