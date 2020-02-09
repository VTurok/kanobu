from django import forms
from .models import Material, Comment
from django.core.exceptions import ValidationError


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'material_type', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'material_type': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }