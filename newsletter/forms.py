from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):

    privacy = forms.BooleanField(required=True)

    class Meta:
        model = Newsletter
        fields = (
            'email',
            'privacy',
        )
