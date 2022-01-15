from django.http import HttpResponse

class StripeWH_Handler():
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
        print(f'event data object: {event.data.object}')
        print(f'event data object: {event.data.object.charges}')
        print(f'event data object: {event.data.object.charges.data[0].billing_details}')
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
   