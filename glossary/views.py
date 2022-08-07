from django.shortcuts import render
from .models import Terms
from django.contrib import messages

# Create your views here.


def view_glossary(request):
    """
    A view to return the blog page
    """
    terms = Terms.objects.all()

    context = {
        'terms': terms,
    }

    return render(request, 'glossary.html', context)