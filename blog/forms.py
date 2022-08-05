"""
Django forms
"""
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    '''
    Form to add a comment and
    insert a sentiment
    '''
    class Meta:
        """
        Link for to model, set fields and labels
        """
        model = Comment
        fields = ('body',)
        labels = {
            "body": "Share your idea on this post",
        }