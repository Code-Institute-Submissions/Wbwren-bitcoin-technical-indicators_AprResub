from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from metrics.models import BitcoinPrice
from .forms import BitcoinForm


# Create your views here.
"""Retreives bitcoin price data from Metrics module and renders it for the view"""

def admincrud(request):
    """A view to return the index page"""
    btc = BitcoinPrice.objects.all()
    context = {
        "btc": btc,
    }
    print(f"contect = {context}")
    return render(request, "admincrud/admincrud.html", context)


def delete_date(request, date):
    get_object_or_404(BitcoinPrice, date=date).delete()
    return redirect(reverse("admincrud"))


def edit_date(request, date):
    """Edit daily price data"""
    day = get_object_or_404(BitcoinPrice, date=date)
    if request.method == "POST":
        form = BitcoinForm(request.POST, request.FILES, instance=day)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated price!")
            return redirect(reverse("admincrud"))
        else:
            messages.error(
                request, "Failed to update price. Please ensure the form is valid."
            )
    else:
        form = BitcoinForm(instance=day)
        messages.info(request, f"You are editing {day.date}")

    template = "admincrud/edit_price_data.html"
    context = {
        "form": form,
        "date": day.date,
    }

    return render(request, template, context)


def add_price_data(request):
    """Add new price data"""
    if request.method == "POST":
        form = BitcoinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added date!")
            return redirect(reverse("add_price_data"))
        else:
            messages.error(
                request, "Failed to add price. Please ensure the form is valid."
            )
    else:
        form = BitcoinForm()

    template = "admincrud/add_price_data.html"
    context = {
        "form": form,
    }

    return render(request, template, context)
