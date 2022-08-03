from django import forms
from .models import Algo, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Algo
        fields = '__all__'

    # Make changes to the fields: categories showing
    # with their friendly name
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
    
    