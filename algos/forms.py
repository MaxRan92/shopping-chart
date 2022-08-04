from django import forms
from .widgets import CustomClearableFileInput
from .models import Algo, Category, Comment


class AlgoForm(forms.ModelForm):

    class Meta:
        model = Algo
        fields = '__all__'

    image = forms.ImageField(label='image', required=False, widget=CustomClearableFileInput)

    # Make changes to the fields: categories showing
    # with their friendly name
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
    

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
            "body": "Share your idea on this ticker",
        }