from asyncio.windows_events import NULL
from django.http import HttpResponse
from home.models import Profile
from django.shortcuts import get_object_or_404


class StripeWH_Handler:
    """Handle Stripe webhooks"""
    
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print('test here')
        print(self.request)
        print(self.request.user.email)
        profile = get_object_or_404(Profile, email=self.request.user.email)
        print(f'profile email: {profile.email}')
        print(f'profile premium member: {profile.premium_member}')
        profile.premium_member = True
        profile.save()
        print(f'profile premium member: {profile.premium_member}')
        return HttpResponse(
            content=f'Webhook: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook: {event["type"]}',
            status=200)
   