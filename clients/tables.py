import django_tables2 as tables
from clients.models import Client

TEMPLATE = """
<button class = "edit-button" value="{{record.id_client}}">Edytuj</button>
"""
EMAIL = """{% load staticfiles %}
<button class = "email-button" value="{{record.id_client}}"><img class = "email-icon" src = "{% static "clients/images/mail.png" %}"></button>
"""
RESERVATION = """
<button class = "client-reservation-button" value="{{record.id_client}}">Zarezerwuj</button>
"""


class ClientTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='id_client')
    edit = tables.TemplateColumn(TEMPLATE )
    napisz = tables.TemplateColumn(EMAIL)
    zarezerwuj = tables.TemplateColumn(RESERVATION)
    class Meta:
        model = Client
        fields = ( 'first_name', 'last_name', 'sex', 'address.street', 'address.house_no', 'address.apartment_no', 'address.city', 'address.zip', 'address.phone', 'address.email')
        sequence = ('selection', '...')
        template = 'django_tables2/bootstrap.html'
