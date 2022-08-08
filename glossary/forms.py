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


class EditForm(forms.ModelForm):
    '''
    Form to edit the body of a comment
    '''
    class Meta:
        """
        Link for to model, set fields and labels
        """
        model = Terms
        fields = ('term', 'description',)
        labels = {
            "body": "Edit the term and click post to submit",
        }
