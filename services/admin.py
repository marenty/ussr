from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(SeDict)
class SeDictAdmin(admin.ModelAdmin):
    list_display = ('id_se_dict', 'se_dict_name', 'se_group', 'base_price')
    list_filter = ('se_group',)
    fields = ('id_se_dict', 'se_dict_name', 'se_group', 'base_price', 'continous', 'notes')
admin.site.register(SeDict, SeDictAdmin)

admin.site.register(SeDiscount)
admin.site.register(SeRequirement)

class ServiceAdmin(admin.ModelAdmin):
    # TODO w rzeczywistosci dobrze by pociagnac nazwe serwisu, nie kod i imie/nazwisko/nazwe klienta,
    # a nie jego id
    list_display = ('id_service', 'service_code', 'client')
    search_fields = ('id_service', 'service_code', 'client')
    list_filter = ('service_code',)
    ordering = ('created_datetime',)
    fields = ('is_confirmed', 'service_code', 'client', 'location', 'create_invoice', 'min_start_datetime', 'planned_start', 'planned_end', 'notes')
admin.site.register(Service, ServiceAdmin)

admin.site.register(SeGroupDict)
