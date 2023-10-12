from django import forms
from .models import Ad, AdType


def _ad_type_choices():
  ad_types = AdType.objects.all()
  data = []
  for ad_type in ad_types:
    data.append((ad_type.id, ad_type.name))

  return data


class AdTypeForm(forms.Form):
  ad_type = forms.ChoiceField(widget=forms.Select, choices=_ad_type_choices())


class AdForm(forms.Form):
  actual_spend = forms.DecimalField(decimal_places=2, max_digits=14, widget=forms.NumberInput)
  date = forms.DateField(widget=forms.TextInput(attrs={"class": "form-control", "type":"date"}))
  ad_type = forms.CharField(widget=forms.HiddenInput, required=True, initial=0)
