from django.shortcuts import render
from metrics.models import Bitcoin_Price_Data, Metric

# Create your views here.
# def administrator(request):
#     """ A view to return all metrics """

#     btc = Bitcoin_Price_Data.objects.all()
    
#     context = {
#         'btc': btc,
#         }
#     return render(request, 'admin_crud/administrator.html', context)

def administrator(request):
    """ A view to return all metrics """

    metrics = Metric.objects.all()
 
    context = {
        'metrics': metrics,

        }
    return render(request, 'metrics/metrics.html', context)