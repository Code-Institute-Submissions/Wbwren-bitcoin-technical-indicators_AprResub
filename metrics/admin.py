from django.contrib import admin
from .models import Metric, Bitcoin_Price_Data

# Register your models here.
class MetricAdmin(admin.ModelAdmin):
    list_display = (
         'friendly_name',
         'name',
         'price',
         'description',
    )

class PriceAdmin(admin.ModelAdmin):
    list_display = (
         "date",
         "open",
         "price",
         "high",
         "low",
    )


admin.site.register(Metric, MetricAdmin)
admin.site.register(Bitcoin_Price_Data, PriceAdmin)