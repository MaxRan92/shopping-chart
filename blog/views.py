from django.shortcuts import render
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
