import django_tables2 as tables
from utilities.models import ResourcesUsage
TEMPLATE = """
<button class = "resignation-button" value="{{record.id_resources_usage}}">Zrezygnuj</button>
"""


class ClientServicesTable(tables.Table):

    service_name = tables.Column(accessor = 'service.service_code.se_dict_name')
    service_detetime_start = tables.Column(accessor = 'service.planned_start')
    service_detetime_end = tables.Column(accessor = 'service.planned_end')
    service_price = tables.Column(accessor = 'service.service_code.base_price')
    employee_name = tables.Column(accessor = 'worker.get_employee_name', orderable = False)
    resignation_button = tables.TemplateColumn(TEMPLATE, verbose_name = '')

    class Meta:
        model = ResourcesUsage
        fields = {}
        template = 'django_tables2/bootstrap.html'


class ClientFinishedServicesTable(tables.Table):

    service_name = tables.Column(accessor = 'service.service_code.se_dict_name')
    service_detetime_start = tables.Column(accessor = 'service.planned_start')
    service_detetime_end = tables.Column(accessor = 'service.planned_end')
    service_price = tables.Column(accessor = 'service.service_code.base_price')
    employee_name = tables.Column(accessor = 'worker.get_employee_name', orderable = False)

    class Meta:
        model = ResourcesUsage
        fields = {}
        template = 'django_tables2/bootstrap.html'

class WorkerServicesTable(tables.Table):

    service_name = tables.Column(accessor = 'service.service_code.se_dict_name')
    service_detetime_start = tables.Column(accessor = 'service.planned_start')
    service_detetime_end = tables.Column(accessor = 'service.planned_end')
    service_price = tables.Column(accessor = 'service.service_code.base_price')
    client_first_name = tables.Column(accessor = 'service.client.first_name')
    client_last_name = tables.Column(accessor = 'service.client.last_name')

    class Meta:
        model = ResourcesUsage
        fields = {}
        template = 'django_tables2/bootstrap.html'

class AllServicesTable(tables.Table):

    service_name = tables.Column(accessor = 'service.service_code.se_dict_name')
    service_detetime_start = tables.Column(accessor = 'service.planned_start')
    service_detetime_end = tables.Column(accessor = 'service.planned_end')
    service_price = tables.Column(accessor = 'service.service_code.base_price')
    client_first_name = tables.Column(accessor = 'service.client.first_name')
    client_last_name = tables.Column(accessor = 'service.client.last_name')

    class Meta:
        model = ResourcesUsage
        fields = {}
        template = 'django_tables2/bootstrap.html'
