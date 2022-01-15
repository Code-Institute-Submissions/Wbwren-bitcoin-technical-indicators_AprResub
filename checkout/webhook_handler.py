from django.http import HttpResponse

from home.models import Profile


def testFunc():
    print('in my test function ##################################')

class StripeWH_Handler:
    """Handle Stripe webhooks"""
    print('in wh handler func ##################################')
    
    #day = get_object_or_404(Profile, email=email)
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        print('handle funct')
        return HttpResponse(
            content=f'Unhandled webhook: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print('handle intent success')
        testFunc()


        return HttpResponse(
            content=f'Webhook: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        print('handle funct payment failed')
        return HttpResponse(
            content=f'Webhook: {event["type"]}',
            status=200)
    
    print('bottom of wh handler fucnt((((((')

   