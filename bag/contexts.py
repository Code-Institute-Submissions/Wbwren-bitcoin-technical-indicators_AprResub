from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from metrics.models import Metric

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        metric = get_object_or_404(Metric, pk=item_id)
        total += quantity * metric.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'metric': metric,
        })


    
    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
    }

    return context