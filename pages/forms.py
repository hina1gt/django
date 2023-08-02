from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'title', 'image', 'description', 'price', 'author', 'condition'

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = '__all__'