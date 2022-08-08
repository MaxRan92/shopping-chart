from django.shortcuts import render, reverse, redirect
from .models import Terms
from .forms import TermForm, EditForm
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


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

        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        return super(TermDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        view_glossary.term_deleted = True
        return reverse("view_terms")


@method_decorator(login_required, name="dispatch")
class TermEdit(UpdateView):
    """
    If user is logged in:
    Direct user to update_comment.html template,
    displaying ReviewForm for that specific review.
    Post edited info back to the DB and return user to post.
    """
    model = Terms
    form_class = EditForm
    template_name = "edit_term.html"

    def check_superuser(self, request):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

    def form_valid(self, form):
        """
        Upon success prompt the user with a success message.
        """
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, *args, **kwargs):
        """
        Upon success returns user to the stock detail page.
        """
        return reverse("view_terms")
