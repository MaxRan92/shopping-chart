from django.shortcuts import render, get_object_or_404
from .models import Post
from shopping_chart.settings import MEDIA_URL
from django.views import generic, View

# Create your views here.

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

def post_detail(request, post_id):
    """ A view to show a single blog post """

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
            },
        )
