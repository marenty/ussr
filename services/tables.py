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
    employee_name = tables.Column(accessor = 'worker.get_employee_name')
    resignation_button = tables.TemplateColumn(TEMPLATE)

    class Meta:
        model = ResourcesUsage
        fields = {}
        template = 'django_tables2/bootstrap.html'

class WorkerServicesTable(tables.Table):

    service_name = tables.Column(accessor = 'service.service_code.se_dict_name')
    service_detetime_start = tables.Column(accessor = 'service.planned_start')
    service_detetime_end = tables.Column(accessor = 'service.planned_end')
    service_price = tables.Column(accessor = 'service.service_code.base_price')
    employee_name = tables.Column(accessor = 'worker.get_employee_name')

    class Meta:
        model = ResourcesUsage
        fields = {}
        template = 'django_tables2/bootstrap.html'
