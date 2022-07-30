from django.shortcuts import render, redirect

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

    licensing_period = int(request.POST.get('licensing_period'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list (bag.keys()):
        bag[item_id] += licensing_period
    else:
        bag[item_id] = licensing_period

    request.session['bag'] = bag
    return redirect(redirect_url)