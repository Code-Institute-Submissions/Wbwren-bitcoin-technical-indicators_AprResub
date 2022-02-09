from django import forms
from metrics.models import BitcoinPriceData


class BitcoinForm(forms.ModelForm):
    class Meta:
        model = BitcoinPriceData
        verbose_name_plural = "Bitcoin price data"
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dates = BitcoinPriceData.objects.all()
        friendly_names = [(d.id, d.date) for d in dates]

        self.fields["date"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
