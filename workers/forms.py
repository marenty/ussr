from django import forms
from django.forms import ModelForm
from .models import Worker
from utilities.models import Address

class WorkerNameForm(forms.Form):
    first_name = forms.CharField(label='Imię', max_length=20)
    last_name = forms.CharField(label='Nazwisko', max_length=20)


class WorkerAddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['email', 'phone', 'street', 'house_no', 'apartment_no', 'city', 'zip' ]


class WorkerPersonalInformationsForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name']
