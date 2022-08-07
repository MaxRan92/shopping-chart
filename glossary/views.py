from django.shortcuts import render, reverse, redirect
from .models import Terms
from .forms import TermForm
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.


def view_glossary(request):
    """
    A view to return the glossary page
    """
    
    terms = Terms.objects.all()
    form = TermForm(request.POST or None)

    # if term_deleted:
    #     messages.success(request, f'The term has been deleted!')
    #     term_deleted = False

    if request.method == 'POST':
        form = TermForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'The new term has been submitted')
            return redirect(reverse('view_terms'))

    context = {
        'terms': terms,
        'form': form,
    }
    
    return render(request, 'glossary.html', context)


@method_decorator(login_required, name="dispatch")
class TermDelete(DeleteView):
    """
    If user is logged in:
    If is superuser, delete the term
    """
    model = Terms
    template_name = "delete_term.html"

    def delete(self, request, *args, **kwargs):
        return super(TermDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        view_glossary.term_deleted = True
        return reverse("view_terms")