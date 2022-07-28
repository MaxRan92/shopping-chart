from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Algo, Category
from shopping_chart.settings import MEDIA_URL

# Create your views here.

def all_algos(request):
    """
    A view to show all products, including sorting and search queries
    """

    algos = Algo.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            algos = algos.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any serach criteria!")
                return redirect(reverse('algos'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            algos = algos.filter(queries)

    context = {
        'algos': algos,
        'MEDIA_URL': MEDIA_URL,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'algos/algos.html', context)


def algo_detail(request, algo_id):
    """
    A view to show the detailed page of one algorithm
    """

    algo = get_object_or_404(Algo, pk=algo_id)

    context = {
        'algo': algo,
        'MEDIA_URL': MEDIA_URL,
    }

    return render(request, 'algos/algo_detail.html', context)
