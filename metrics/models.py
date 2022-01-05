from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DecimalField
from django.utils.translation import gettext as _

# Create your models here.
class Metric(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Bitcoin_Price_Data(models.Model):
    date = models.DateField(_("date"))
    open = models.FloatField(_("open"))
    price = models.FloatField(_("price"))
    high = models.FloatField(_("high"))
    low = models.FloatField(_("low"))

class Metric_Data(models.Model):
    date = models.DateField(_("date"))
    pi_cycle_top = models.FloatField(_("pi_cycle_top"), null=True, blank=True)
    ma200w = models.FloatField(_("200WMA"), null=True, blank=True)
    ma50d_50w = models.FloatField(_("ma50D_50w"), null=True, blank=True)
    risk_indicator = models.FloatField(_("risk_indicator"), null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name