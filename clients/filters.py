from .tables import ClientTable
from .models import Client

import django_filters

class ClientTableFilter(django_filters.FilterSet):

    address__email = django_filters.CharFilter(lookup_expr='contains', label = 'E-mail:')

    class Meta:
        model = Client
        fields = [ 'first_name','last_name', 'address__street', 'address__house_no' , 'address__apartment_no' ,
                     'address__city', 'address__zip', 'address__phone', 'address__email' ]
