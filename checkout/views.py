from django.shortcuts import render, redirect
import stripe
from home.context_processor import is_premium_member

from bitcoin_technical_indicators.settings import STRIPE_SECRET_KEY


def checkout(request):
    try:
        stripe.api_key = STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "Risk Metric",
                        },
                        "unit_amount": 15000,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url="https://bitcoin-technical-indicators.herokuapp.com/checkout/checkout_successful",
            cancel_url="https://bitcoin-technical-indicators.herokuapp.com/checkout/checkout_unsuccessful",
        )
    except:
        checkout_unsuccessful(request)
        return checkout_unsuccessful(request)
    return redirect(session.url, code=303)

def premium_access_detail(request):
    request = is_premium_member(request)
    return render(request, "checkout/premium_access_detail.html")


def checkout_successful(request):
    request = is_premium_member(request)
    return render(request, "checkout/checkout_successful.html")


def checkout_unsuccessful(request):
    request = is_premium_member(request)
    return render(request, "checkout/checkout_unsuccessful.html")
