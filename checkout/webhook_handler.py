from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from home.models import Profile


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        print('handling evert here ************************')
        profile = get_object_or_404(Profile, user_id=1)
        profile.premium_member = True
        profile.save()
        return HttpResponse(content=f'Unhandled webhook: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print('test here')
        #print(event.data.object.charges.data[0].billing_details.email)
        # id = 0
        # email = event.data.object.charges.data[0].billing_details.email
        # users = User.objects.all()
        # for user in users:
        #     if user.email == email:
        #         id = user.id

        
        profile = get_object_or_404(Profile, user_id=1)
        profile.premium_member = True
        profile.save()

        return HttpResponse(content=f'Webhook: {event["type"]}', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        print('fail *(*************')
        profile = get_object_or_404(Profile, user_id=1)
        profile.premium_member = True
        profile.save()
        return HttpResponse(content=f'Webhook: {event["type"]}', status=200)
