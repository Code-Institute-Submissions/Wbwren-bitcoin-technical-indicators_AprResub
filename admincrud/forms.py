from django import forms
from metrics.models import BitcoinPrice
from metrics.models import Metric


class BitcoinForm(forms.ModelForm):
    class Meta:
        model = BitcoinPrice
        verbose_name_plural = "Bitcoin price data"
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dates = BitcoinPrice.objects.all()
        friendly_names = [(d.date) for d in dates]

        self.fields["date"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class MetricForm(forms.ModelForm):
    class Meta:
        model = Metric
        verbose_name_plural = "Metrics"
        fields = ("display_name", "description", "instructions")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        metrics = Metric.objects.all()
        friendly_names = [(metric.display_name) for metric in metrics]

        self.fields["display_name"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
