from django.db import models
from django.utils.translation import gettext as _


"""Model containing details of all bitcoin metrics"""
class Metric(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description_short = models.TextField()
    description_long = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_path = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


"""Model containing bitcoin price data"""
class BitcoinPrice(models.Model):
    date = models.DateTimeField(_("date"), primary_key=True)
    price = models.FloatField(_("price"))
    class Meta: 
        verbose_name = "Bitcoin Price"
        verbose_name_plural = "Bitcoin Price"
    