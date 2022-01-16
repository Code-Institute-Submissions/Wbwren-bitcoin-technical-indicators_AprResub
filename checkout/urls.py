from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path("", views.checkout, name="checkout"),
    path("premium_access_detail", views.premium_access_detail, name="premium_access_detail"),
    path("create_checkout_session", views.checkout, name="create_checkout_session"),
    path("checkout_successful", views.checkout_successful, name="checkout_successful"),
    path(
        "checkout_unsuccessful",
        views.checkout_unsuccessful,
        name="checkout_unsuccessful",
    ),
    path("wh/", webhook, name="webhook"),
]
