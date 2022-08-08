from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.contrib import messages
from shopping_chart.settings import MEDIA_URL
from django.views import View
from django.views.generic import DeleteView, UpdateView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CommentForm, EditForm


def view_blog(request):
    """
    A view to return the blog page
    """
    posts = Post.objects.all()

    context = {
        'posts': posts,
        'MEDIA_URL': MEDIA_URL,
    }

    return render(request, 'blog.html', context)


class PostDetail(View):

    # Variables declaration
    comment_deleted = comment_edited = comment_created = False

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('-created_on')

        if self.comment_deleted:
            messages.success(request, 'Your comment has been deleted!')
            PostDetail.comment_deleted = False
        elif self.comment_edited:
            messages.success(request, 'Your comment has been updated!')
            PostDetail.comment_edited = False

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm,
                "blog_message": True,
            },
        )

    def post(self, request, slug):
        """
        Post method to post the comment.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('-created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been posted!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "blog_message": True,
                "comment_form": CommentForm,
            },
        )


@method_decorator(login_required, name="dispatch")
class CommentDelete(DeleteView):
    """
    If user is logged in:
    Direct user to delete_comment.html template
    User will be prompted with a message to confirm.
    """
    model = Comment
    template_name = "delete_comment.html"

    def delete(self, request, *args, **kwargs):
        return super(CommentDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        PostDetail.comment_deleted = True
        return reverse("post_detail", kwargs={"slug": self.object.post.slug})


@method_decorator(login_required, name="dispatch")
class CommentEdit(UpdateView):
    """
    If user is logged in:
    Direct user to update_comment.html template,
    displaying ReviewForm for that specific review.
    Post edited info back to the DB and return user to post.
    """
    model = Comment
    form_class = EditForm
    template_name = "edit_comment.html"

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
        PostDetail.comment_edited = True
        return reverse("post_detail", kwargs={"slug": self.object.post.slug})
