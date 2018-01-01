from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .tables import AllServicesTable
from utilities.models import ResourcesUsage

import django_filters

class ResourcesUsageFilter(django_filters.FilterSet):
    start_timestamp = django_filters.DateFilter(lookup_expr='gte')
    finish_timestamp = django_filters.DateFilter(lookup_expr='lte')

    class Meta:
        model = ResourcesUsage
        fields = [ 'service__client__first_name' , 'start_timestamp', 'finish_timestamp']

class FilteredResourceUsageListView(SingleTableMixin, FilterView):
    table_class = AllServicesTable
    model = ResourcesUsage
    template_name = 'worker_services.html'

    filterset_class = ResourcesUsageFilter
