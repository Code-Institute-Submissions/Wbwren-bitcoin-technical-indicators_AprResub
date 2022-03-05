from django.contrib import admin
from .models import Metric, BitcoinPrice

class MetricAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
        "price",
        "description_short",
    )


class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "price",
    )


admin.site.register(Metric, MetricAdmin)
admin.site.register(BitcoinPrice, PriceAdmin)
