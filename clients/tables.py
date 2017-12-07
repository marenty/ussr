import django_tables2 as tables
from clients.models import Client

TEMPLATE = """
<button class = "edit-button" value="{{record.id_client}}">Edytuj</button>
"""

class ClientTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='id_client')
    edit = tables.TemplateColumn(TEMPLATE )
    class Meta:
        model = Client
        fields = ( 'first_name', 'last_name', 'sex', 'address.street', 'address.house_no', 'address.apartment_no', 'address.city', 'address.zip', 'address.email')
