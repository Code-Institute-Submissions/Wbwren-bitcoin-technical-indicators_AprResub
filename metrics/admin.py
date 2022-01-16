from django.contrib import admin
from .models import Metric, Metric_Data, Bitcoin_Price_Data

# Register your models here.
class MetricAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
        "price",
        "description_short",
    )


class MetricDataAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "pi_cycle_top",
        "ma200w",
        "ma50d_200d",
        "risk_indicator",
    )


class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "open",
        "price",
        "high",
        "low",
    )


admin.site.register(Metric, MetricAdmin)
admin.site.register(Metric_Data, MetricDataAdmin)
admin.site.register(Bitcoin_Price_Data, PriceAdmin)
