from django.shortcuts import get_object_or_404, render
from .models import Metric
from plotly.offline import plot
import plotly.express as px
from plotly.graph_objs import *
from metrics.models import BitcoinPrice
import pandas as pd
from home.context_processor import is_premium_member


def all_metrics(request):
    """A view to return all metrics"""

    if request.user.is_anonymous:
        return render(request, "home/index.html")

    metrics = Metric.objects.all()

    context = {
        "metrics": metrics,
        "is_premium_member" : is_premium_member(request),
    }

    return render(request, "metrics/metrics.html", context)


def metric_detail(request, metric_name):
    """View to display an individual metric"""
    if request.user.is_anonymous:
        return render(request, "home/index.html")


    if not is_premium_member(request) and metric_name == 'risk_indicator':
        return render(request, "checkout/premium_access_detail.html")

    # Connect to database and retrieve bitcoin price data
    # query result must be reversed so that the moving averages are
    # calculated in the correct direction
    df = pd.DataFrame(reversed(list(BitcoinPrice.objects.all().values())))
   
    # Calculate moving averages using dataframe
    df["111DMA"] = df.iloc[:, 1].rolling(window=111).mean()
    df["350DMA*2"] = (df.iloc[:, 1].rolling(window=350).mean()) * 2
    df["350DMA"] = df.iloc[:, 1].rolling(window=350).mean()
    df["200WMA"] = df.iloc[:, 1].rolling(window=1400).mean()
    df["50DMA"] = df.iloc[:, 1].rolling(window=50).mean()
    df["200DMA"] = df.iloc[:, 1].rolling(window=200).mean()

    # Calculate the Simple moving average ratio
    df["SMAR"] = df["50DMA"] / df["350DMA"]

    fig = px.line(df, x="date", y=df["price"])

    
    metric = get_object_or_404(Metric, name=metric_name)
    
    
    # Check which metric is selected and add the appropritate moving averages
    if metric.name == "risk_indicator":
        fig.add_scatter(name="SMAR", x=df["date"], y=df["SMAR"], line_color="green")
        fig.add_hline(y=0.9, line_color="red")
    elif metric.name == "50DMA_200DMA":
        fig.add_scatter(name="50DMA", x=df["date"], y=df["50DMA"])
        fig.add_scatter(name="200DMA", x=df["date"], y=df["200DMA"])
    elif metric.name == "200WMA":
        fig.add_scatter(name="200WMA", x=df["date"], y=df["200WMA"])
    elif metric.name == "pi_cycle_top":
        fig.add_scatter(name="111DMA", x=df["date"], y=df["111DMA"])
        fig.add_scatter(name="350DMA*2", x=df["date"], y=df["350DMA*2"])
        fig.add_vline(
            x="2013-12-01", line_dash="dash", line_width=2, line_color="green"
        )
        fig.add_vline(
            x="2017-12-16", line_dash="dash", line_width=2, line_color="green"
        )
        fig.add_vline(
            x="2013-04-05", line_dash="dash", line_width=2, line_color="green"
        )
        fig.add_vline(
            x="2021-04-11", line_dash="dash", line_width=2, line_color="green"
        )
    else:
        return render(request, "home/index.html")

    # Set the y axis to a logarithmic scale
    fig.update_yaxes(type="log", range=[-1, 5])

    # Get HTML needed to render the plot.
    plot_div = plot({"data": fig}, output_type="div")

    context={
        "plot_div": plot_div,
        "is_premium_member": is_premium_member(request),
        "metric": metric
    }
    
    return render(request, "metrics/metric_detail.html", context)
