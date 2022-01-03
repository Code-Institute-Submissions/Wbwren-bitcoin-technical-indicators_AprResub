from django.contrib import admin
from .models import Metric

# Register your models here.
class MetricAdmin(admin.ModelAdmin):
    list_display = (
         'friendly_name',
         'name',
         'price',
         'description',
    )


admin.site.register(Metric, MetricAdmin)