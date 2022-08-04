from django.shortcuts import render

# Create your views here.

def view_blog(request):
    """
    A view to return the blog page
    """
    return render(request, 'blog.html')

