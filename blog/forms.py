"""
Django forms
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    Form to add a comment
    '''
    class Meta:
        """
        Link for to model, set fields and labels
        """
        model = Comment
        fields = ('body', 'user_rating', )
        labels = {
            "body": "Share your idea on this post",
            "user_rating": "Give a rating to the post",
        }


class EditForm(forms.ModelForm):
    '''
    Form to edit the body of a comment
    '''
    class Meta:
        """
        Link for to model, set fields and labels
        """
        model = Comment
        fields = ('body', 'user_rating', )
        labels = {
            "body": "Change the comment and click post to submit",
            "user_rating": "Change the rating given to the post"
        }
