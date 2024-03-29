"""
Credits: the code is inspired and adapted from the
Code Institute Boutique Ado Project
"""
from django.shortcuts import render, redirect, reverse
from newsletter.forms import NewsletterForm
from newsletter.models import Newsletter
from django.contrib import messages


def index(request):
    """ A view to return the index page """

    form = NewsletterForm(request.POST or None)

    if request.method == 'POST':
        print(form.errors)
        if form.is_valid:
            form.save()
            messages.success(request, 'Thank you for subscribing \
                to our newsletter!')
            return redirect(reverse('home'))
        messages.error(request, 'There was an error please try again')

    context = {
        'form': form,
    }

    return render(request, 'home/index.html', context)
