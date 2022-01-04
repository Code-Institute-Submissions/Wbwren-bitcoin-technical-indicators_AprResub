from django.shortcuts import get_object_or_404, render
from .models import Metric
import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd


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
    """ 
    View demonstrating how to display a graph object
    on a web page with Plotly. 
    """
    
    # Generating some data for plots.
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

    fig = go.Figure(data=[go.Candlestick(
        x=df['Date'],
        open=df['AAPL.Open'], high=df['AAPL.High'],
        low=df['AAPL.Low'], close=df['AAPL.Close'],
        increasing_line_color= 'cyan', decreasing_line_color= 'gray'
    )])

    fig.update_layout(
        title='Bitcoin Data',
        yaxis_title='Price',
        shapes = [dict(
            x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
            line_width=2)],
        annotations=[dict(
            x='2016-12-09', y=0.05, xref='x', yref='paper',
            showarrow=False, xanchor='left', text='Increase Period Begins')]
    )

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': fig}, 
                    output_type='div')

    return render(request, 'metrics/metric_detail.html', 
                  context={'plot_div': plot_div})