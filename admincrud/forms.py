from django import forms
from metrics.models import Bitcoin_Price_Data


class BitcoinForm(forms.ModelForm):
    class Meta:
        model = Bitcoin_Price_Data
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dates = Bitcoin_Price_Data.objects.all()
        friendly_names = [(d.id, d.date) for d in dates]

        self.fields["date"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
