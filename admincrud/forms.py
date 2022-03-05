from django import forms
from metrics.models import BitcoinPrice


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
            field.widget.attrs["class"] = "border-black rounded-0"
