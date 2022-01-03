from django.shortcuts import get_object_or_404, render
from .models import Metric

# Create your views here.

def all_metrics(request):
    """ A view to return all metrics """

    metrics = Metric.objects.all()
    context = {
        'metrics': metrics
        }

    return render(request, 'metrics/metrics.html', context)


def metric_detail(request, metric_id):
    """ A view to show and individual metric """

    metric = get_object_or_404(Metric, pk=metric_id)
    context = {
        'metric': metric
        }

    return render(request, 'metrics/metric_detail.html', context)