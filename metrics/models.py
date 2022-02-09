from email.mime import image
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
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


class BitcoinPriceData(models.Model):
    date = models.DateField(_("date"))
    price = models.FloatField(_("price"))
    class Meta: 
        verbose_name = "Bitcoin Price Data"
        verbose_name_plural = "Bitcoin Price Data"
    