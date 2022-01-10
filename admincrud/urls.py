from django.urls import path
from . import views

urlpatterns = [
    path('', views.admincrud, name='admincrud'),
    path('<date>', views.delete_date, name='delete_date'),
]
