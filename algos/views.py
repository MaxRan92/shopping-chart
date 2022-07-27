from django.shortcuts import render
from .models import Algo

# Create your views here.

def all_algos(request):
    """
    A view to show all products, including sorting and search queries
    """

    algos = Algo.objects.all()

    context = {
        'algos': algos,
    }

    return render(request, 'algos/algos.html', context)
