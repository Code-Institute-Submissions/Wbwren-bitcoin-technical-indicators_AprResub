import uuid
from django.db import models
from django.db.models import Sum


class Order(models.Model):
    order_number = models.CharField(max_length = 32, null = False, 
    editable = False)
    email = models.EmailField(max_length = 254, null = False, blank = False)
    date = models.DateTimeField(auto_now_add = True)
    order_total = models.DecimalField(
        max_digits = 10, decimal_places = 2, null = False, default = 0)


    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()


    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum("lineitem_total"))[
            "lineitem_total__sum"]

        self.save()


    def save(self, * args, ** kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save( * args, ** kwargs)


    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null = False,
        blank = False,
        on_delete = models.CASCADE,
        related_name = "lineitems",)

    lineitem_total = models.DecimalField(
        max_digits = 6, decimal_places = 2, null = False, blank = False, 
        editable = False)


    def save(self, * args, ** kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = 50 * self.quantity
        super().save( * args, ** kwargs)


    def __str__(self):
        return f"SKU remove me on order {self.order.order_number}"
