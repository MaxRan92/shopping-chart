from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    discount_perc = settings.DISCOUNT_PERCENTAGE

    if total < settings.DISCOUNT_THRESHOLD:
        discount_abs = 0
    else:
        discount_abs = total * (1 - Decimal(discount_perc / 100))
    
    grand_total = total - discount_abs

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount_abs': discount_abs,
        'discount_perc': discount_perc,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context