from django.shortcuts import get_object_or_404, render
from numpy import log
import numpy
from pandas.core.frame import DataFrame
from .models import Metric, Bitcoin_Price_Data
from home.models import Profile, User
import plotly.graph_objects as go
from plotly.offline import plot
import plotly.express as px
from plotly.graph_objs import *
import sqlite3
import pandas as pd


# Create your views here.

def all_metrics(request):
    """ A view to return all metrics """

    metrics = Metric.objects.all()
    profiles = Profile.objects.all()
    users = User.objects.all()
    context = {
        'metrics': metrics,
        'users': users,
        'profiles': profiles,
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
    

    # Calculate moving averages using dataframe
    df['111DMA'] = df.iloc[:,1].rolling(window=111).mean()
    df['350DMA*2'] = (df.iloc[:,1].rolling(window=350).mean())*2
    df['200WMA'] = df.iloc[:,1].rolling(window=200).mean()
    df['50DMA'] = df.iloc[:,1].rolling(window=50).mean()
    df['350DMA'] = df.iloc[:,1].rolling(window=350).mean()


    fig = px.line(df, x='date', y=df['price'])
    fig.add_scatter(name='111DMA', x=df['date'], y=df['111DMA'])
    fig.add_scatter(name='350DMA*2', x=df['date'], y=df['350DMA*2'])
    fig.add_scatter(name='200WMA', x=df['date'], y=df['200WMA'])
    fig.add_scatter(name='50DMA', x=df['date'], y=df['50DMA'])
    fig.add_scatter(name='350DMA', x=df['date'], y=df['350DMA'])

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