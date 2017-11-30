from django.contrib import admin
from .models import *


class MachineAdmin(admin.ModelAdmin):
    list_display = ('id_machine', 'machine_name', 'machine_type', 'service_interval', 'last_service', 'is_operational', 'notes', 'company_branch')
    list_filter = ('machine_type', 'machine_name', 'service_interval', 'is_operational')
    #search_fields = ('machine_type', 'machine_name')
    #prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    #date_hierarchy = 'publish'
    #ordering = ['status', 'publish']

admin.site.register(Machine, MachineAdmin)

class MachineTypeAdmin(admin.ModelAdmin):
    list_display = ('machine_type_name', 'id_machine_type')
    list_filter = ('machine_type_name', 'id_machine_type')
    #search_fields = ('machine_type_name')
    #prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    #date_hierarchy = 'publish'
    #ordering = ['status', 'publish']

admin.site.register(MachineType, MachineTypeAdmin)


#admin.site.register(Machine)
#admin.site.register(MachineType)
