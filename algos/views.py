from django.shortcuts import render
from .models import Algo
from shopping_chart.settings import MEDIA_URL

# Create your views here.

def all_algos(request):
    """
    A view to show all products, including sorting and search queries
    """

    algos = Algo.objects.all()

    context = {
        'algos': algos,
        'MEDIA_URL': MEDIA_URL,
    }

    return render(request, 'algos/algos.html', context)
