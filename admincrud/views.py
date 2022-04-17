from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from metrics.models import BitcoinPrice
from metrics.models import Metric
from .forms import BitcoinForm, MetricForm


"""Retreives bitcoin price data from Metrics module and 
renders it for the view"""


def edit_price(request):
    """A view to return the index page"""

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    btc = BitcoinPrice.objects.all()
    context = {
        "btc": btc,}

    return render(request, "admincrud/edit_price.html", context)


def edit_metric(request):
    """A view to return the index page"""    
    if not request.user.is_superuser:
        return redirect(reverse("home"))

    metrics = Metric.objects.all()
    context = {
        "metrics": metrics,}

    return render(request, "admincrud/edit_metric.html", context)


def delete_date(request, date):
    if not request.user.is_superuser:
        return redirect(reverse("home"))

    get_object_or_404(BitcoinPrice, date = date).delete()
    return redirect(reverse("edit_price"))


def edit_date(request, date):
    """Edit daily price data"""
    if not request.user.is_superuser:
        return redirect(reverse("login"))

    day = get_object_or_404(BitcoinPrice, date = date)
    if request.method == "POST":
        form = BitcoinForm(request.POST, request.FILES, instance=day)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated price!")
            return redirect(reverse("edit_price"))
        else:
            messages.error(
                request, "Failed to update price. Please ensure "+
                "the form is valid."
            )
    else:
        form = BitcoinForm(instance = day)
        messages.info(request, f"You are editing {day.date}")

    template = "admincrud/edit_price_data.html"
    context = {
        "form": form,
        "date": day.date,}

    return render(request, template, context)


def add_price_data(request):
    """Add new price data"""
    if not request.user.is_superuser:
        return redirect(reverse("home"))

    if request.method == "POST":
        form = BitcoinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added date!")
            return redirect(reverse("edit_price"))
        else:
            messages.error(
                request, "Failed to add price. Please ensure the form is valid."
            )
    else:
        form = BitcoinForm()

    template = "admincrud/add_price_data.html"
    context = {
        "form": form,}

    return render(request, template, context)


def edit_metric_data(request, metric):
    """Edit metric data"""

    if not request.user.is_superuser:
        return redirect(reverse("home"))

    metric = get_object_or_404(Metric, name = metric)
    if request.method == "POST":
        form = MetricForm(request.POST, request.FILES, instance = metric)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated price!")
            return redirect(reverse("edit_metric"))
        else:
            messages.error(
                request, "Failed to update price. Please ensure the form is valid."
            )
    else:
        form = MetricForm(instance = metric)
        messages.info(request, f"You are editing {metric.display_name}")

    template = "admincrud/edit_metric_data.html"
    context = {
        "form": form,
        "metric": metric,
    }

    return render(request, template, context)
