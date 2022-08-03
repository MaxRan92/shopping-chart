from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Algo, Category
from django.db.models.functions import Lower
from shopping_chart.settings import MEDIA_URL
from .forms import AlgoForm

# Create your views here.

def all_algos(request):
    """
    A view to show all products, including sorting and search queries
    """

    algos = Algo.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                algos = algos.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            algos = algos.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'algos': algos,
        'MEDIA_URL': MEDIA_URL,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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

def add_algo(request):
    """
    Add a product to the store
    """
    form = AlgoForm()
    template = 'algos/add_algo.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
