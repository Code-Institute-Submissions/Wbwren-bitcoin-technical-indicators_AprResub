from django.db import models
from django.utils.translation import gettext as _


"""Model containing details of all bitcoin metrics"""
class Metric(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    instructions = models.TextField()
    is_premium_metric = models.BooleanField()
    image_path = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name



class BitcoinPrice(models.Model):
    """Model containing bitcoin price data"""
    date = models.DateField(_("date"), primary_key=True)
    price = models.FloatField(_("price"))

    class Meta: 
        verbose_name = "Bitcoin Price"
        verbose_name_plural = "Bitcoin Price"
    