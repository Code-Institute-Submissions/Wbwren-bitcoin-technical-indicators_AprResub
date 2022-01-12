from django.urls import path
from . import views

urlpatterns = [
    path('', views.admincrud, name='admincrud'),
    path('add_price_data/', views.add_price_data, name='add_price_data'),
    path('edit/<date>', views.edit_date, name='edit_date'),
    path('delete/<date>', views.delete_date, name='delete_date'),
]

