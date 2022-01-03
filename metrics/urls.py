from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_metrics, name='metrics'),
    path('<metric_id>', views.metric_detail, name='metric_detail'),
]
