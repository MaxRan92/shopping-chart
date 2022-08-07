from django.shortcuts import render
from .models import Terms
from .forms import TermForm
from django.contrib import messages

# Create your views here.


def view_glossary(request):
    """
    A view to return the blog page
    """
    terms = Terms.objects.all()
    form = TermForm(request.POST or None)

    context = {
        'terms': terms,
        'form': form,
    }

    return render(request, 'glossary.html', context)
