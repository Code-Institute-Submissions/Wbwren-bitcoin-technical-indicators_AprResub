from django.contrib import admin
from .models import Metric, BitcoinPrice

class MetricAdmin(admin.ModelAdmin):
    list_display = (
        "display_name",
        "name",
        "is_premium_metric",
        "description",
    )


class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "price",
    )


admin.site.register(Metric, MetricAdmin)
admin.site.register(BitcoinPrice, PriceAdmin)
