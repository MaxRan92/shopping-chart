"""
Django forms
"""
from django import forms
from .models import Terms

class TermForm(forms.ModelForm):
    '''
    Form to add a comment
    '''
    class Meta:
        """
        Link for to model, set fields and labels
        """
        model = Terms
        fields = ('term', 'description',)
        labels = {
            "description": "Insert description",
        }
