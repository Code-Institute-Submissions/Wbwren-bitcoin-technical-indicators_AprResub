from django.shortcuts import render
from .models import Metric

# Create your views here.

def all_metrics(request):
    """ A view to return all metrics """

    metrics = Metric.objects.all()
    context = {
        'metrics': metrics
        }

    return render(request, 'metrics/metrics.html', context)