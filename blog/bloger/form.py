from django import forms
from .models import Blogers,BlodPost

class BlogerForm(forms.ModelForm):
    class Meta:
        model = Blogers
        fields = ('first_name', 'text','date')

class Add(forms.ModelForm):
    class Meta:
        model = BlodPost
        fields = ('header','first_name', 'text')

class Replacement(forms.ModelForm):
    class Meta:
        model = BlodPost
        fields = ('text',)