from django.contrib import admin
from .models import Metric, BitcoinPriceData

# Register your models here.
class MetricAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
        "price",
        "description_short",
    )


class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "price",
    )


admin.site.register(Metric, MetricAdmin)
admin.site.register(BitcoinPriceData, PriceAdmin)
