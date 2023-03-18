from django import forms
from OnlyTrucks.models import Post, Remolques

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= '__all__'

class RemolquesForm(forms.ModelForm):
    class Meta:
        model=Remolques
        fields= '__all__'