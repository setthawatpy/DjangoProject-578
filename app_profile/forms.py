from django import forms
from .models import *


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('title', 'description', 'stock', 'weight', 'price', 'available', 'picture')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'picture': forms.FileInput(attrs={'class': 'form-control', 'min': 0}),
        }