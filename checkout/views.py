import os
from re import template
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import stripe

from crypto_technicaL_analysis.settings import STRIPE_SECRET_KEY

def checkout(request):
    try:
        session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
            'currency': 'usd',
            'product_data': {
            'name': 'T-shirt',
        },
            'unit_amount': 2000,
        },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/checkout/checkout_successful',
        cancel_url='http://127.0.0.1:8000/checkout/checkout_unsuccessful',
        )
    except:
        checkout_unsuccessful(request)
        return checkout_unsuccessful(request)

    return redirect(session.url, code=303)

def checkout_successful(request):

    return render(request, 'checkout/checkout_successful.html')

def checkout_unsuccessful(request):

    return render(request, 'checkout/checkout_unsuccessful.html')

