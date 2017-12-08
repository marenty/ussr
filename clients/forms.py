from django import forms
from django.forms import ModelForm
from utilities.models import Address
from .models import Client
from django.forms.widgets import HiddenInput


class ClientAddressForm(ModelForm):
    class Meta:
        model = Address
        fields = [ 'email', 'phone', 'street', 'house_no', 'apartment_no', 'city', 'zip' ]


class ClientPersonalInformationsForm(ModelForm):
    class Meta:
        model = Client
        fields = [ 'first_name', 'last_name', 'sex' ]

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Temat')
    message = forms.CharField(widget=forms.Textarea, label='Wiadomośc')
