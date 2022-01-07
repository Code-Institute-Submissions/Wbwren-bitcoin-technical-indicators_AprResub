from django.urls import path
from . import views

urlpatterns = [
    path('', views.admincrud, name='admincrud'),
]
