from django.urls import path
from . import views

urlpatterns = [
    path("edit_metric", views.edit_metric, name="edit_metric"),
    path("edit_metric_data/<metric>", views.edit_metric_data, name="edit_metric_data"),

    path("edit_price", views.edit_price, name="edit_price"),
    path("add_price_data/", views.add_price_data, name="add_price_data"),
    path("edit/<date>", views.edit_date, name="edit_date"),
    path("delete/<date>", views.delete_date, name="delete_date"),
]
