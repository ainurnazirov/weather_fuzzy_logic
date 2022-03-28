from django import forms


class ParametersForm(forms.Form):
    temperature = forms.DecimalField(max_digits=3, decimal_places=1)
    pressure = forms.DecimalField(max_digits=4, decimal_places=1)
    humidity = forms.DecimalField(max_digits=5, decimal_places=2)
