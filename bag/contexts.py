from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from algos.models import Algo

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    discount_perc = settings.DISCOUNT_PERCENTAGE
    bag = request.session.get('bag', {})

    for item_id, licensing_period in bag.items():
        algo = get_object_or_404(Algo, pk=item_id)
        total += licensing_period * algo.price
        bag_items.append({
            'item_id': item_id,
            'licensing_period': licensing_period,
            'algo': algo,
        })

    if total < settings.DISCOUNT_THRESHOLD:
        discount_abs = 0
        discount_delta = settings.DISCOUNT_THRESHOLD - total 
    else:
        discount_abs = total * Decimal(discount_perc / 100)
        discount_delta = 0
    
    grand_total = total - discount_abs

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount_abs': discount_abs,
        'discount_perc': discount_perc,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
        'discount_delta': discount_delta,
    }

    return context