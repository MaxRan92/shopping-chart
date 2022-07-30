from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from algos.models import Algo

# Create your views here.


def view_bag(request):
    """
    A view to renders the bag content page
    """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag
    """

    algo = get_object_or_404(Algo, pk=item_id)
    license_period = int(request.POST.get('license_period'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list (bag.keys()):
        bag[item_id] += license_period
        messages.success(request, f'Updated {algo.name} license period to {bag[item_id]} months')
    else:
        bag[item_id] = license_period
        messages.success(request, f'Added {algo.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product to the specified license period
    """

    algo = get_object_or_404(Algo, pk=item_id)
    license_period = int(request.POST.get('license_period'))
    bag = request.session.get('bag', {})

    if license_period > 0:
        bag[item_id] = license_period
        messages.success(request, f'Updated {algo.name} license period to {bag[item_id]} months')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {algo.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove a specified product from the bag
    """

    try:
        algo = get_object_or_404(Algo, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {algo.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)