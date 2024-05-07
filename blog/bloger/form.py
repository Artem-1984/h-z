from django import forms
from .models import Blogers

class BlogerForm(forms.ModelForm):
    class Meta:
        model = Blogers
        fields = ('first_name', 'text','date')