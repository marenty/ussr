from django import forms

from .models import MachineType, Machine, Worker, Client

class MachineTypeForm(forms.ModelForm):
    class Meta:
        model = MachineType
        fields = ['machine_type_name']
        #labels = {'text': ''}

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machine_name', 'machine_type', 'service_interval', 'last_service', 'is_operational', 'notes']
        #labels = {'text': ''}

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'worker_title', 'active', 'notes']
        #labels = {'text': ''}

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'is_company', 'client_name', 'nip', 'is_blocked', 'blocked_notes',
                  'default_invoice', 'default_reminder_sms_minutes', 'is_confirmed', 'is_rejected', 'ip_address', 'default_reminder_email_minutes',
                  'default_finished_info_sms', 'default_finished_info_email', 'client_discount_percent_sum', 'notes', 'default_company_branch' ]
        #labels = {'text': ''}
