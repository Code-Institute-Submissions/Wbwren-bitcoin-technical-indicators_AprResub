from django.shortcuts import get_object_or_404, render
from numpy import log
from .models import Metric, Bitcoin_Price_Data
import plotly.graph_objects as go
from plotly.offline import plot
import sqlite3
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
    
    # temp = list(Bitcoin_Price_Data.objects.all())
    
    # for item in temp:
    #     print(item.headline)
    conn = sqlite3.connect('db.sqlite3')
    print('conn')
          
    sql_query = pd.read_sql_query('''SELECT * FROM metrics_bitcoin_price_data''', conn)

    df = pd.DataFrame(sql_query, columns = ['date', 'open', 'price', 'high', 'low'])
    print (df)

    fig = go.Figure(data=[go.Candlestick(
        x=df['date'],
        open=df['open'], high=df['high'],
        low=df['low'], close=df['price'],
        increasing_line_color= 'green', decreasing_line_color= 'red'
    )])

    fig.update_layout(
        width=1600, height=800,
        title='Bitcoin Data',
        yaxis_title='Price',
        shapes = [dict(
            x0='2012-12-09', x1='2012-12-09', y0=0, y1=1, xref='x', yref='paper',
            line_width=2)],
        annotations=[dict(
            x='2016-12-09', y=0.05, xref='x', yref='paper',
            showarrow=False, xanchor='left', text='Increase Period Begins')]
    )

    fig.update_yaxes(type="log", range=[-1,5])

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': fig}, 
                    output_type='div')

    return render(request, 'metrics/metric_detail.html', 
                  context={'plot_div': plot_div})