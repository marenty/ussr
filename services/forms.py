from django import forms
import datetime

class ReservationForm(forms.Form):
    service = forms.CharField()
    date = forms.DateTimeField(input_formats=["%Y-%m-%d %H:%M"])
    facture = forms.BooleanField(required=False)
