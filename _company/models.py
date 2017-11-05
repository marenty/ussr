# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ClBlockedReasonDict(models.Model):
    id_cl_blocked_reason_dict = models.CharField(primary_key=True, max_length=10)
    blocked_reason_name = models.CharField(unique=True, max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cl_blocked_reason_dict'
        verbose_name = "Powód blokady"
        verbose_name_plural = "Powody blokady"

    def __str__(self):
        return "[" + self.id_cl_blocked_reason_dict + "]" + " " + self.blocked_reason_name


class ClCommunicationLog(models.Model):
    id_cl_communication_log = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING, db_column='client', blank=True, null=True)
    communication_reason = models.ForeignKey('ClCommunicationReason', models.DO_NOTHING, db_column='communication_reason', blank=True, null=True)
    service = models.ForeignKey('Service', models.DO_NOTHING, db_column='service', blank=True, null=True)
    contact_type = models.ForeignKey('ContactType', models.DO_NOTHING, db_column='contact_type')
    contact_address = models.CharField(max_length=100, blank=True, null=True)
    message_body = models.TextField(blank=True, null=True)
    minutes_before_action = models.IntegerField(blank=True, null=True)
    notes = models.IntegerField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=10, blank=True, null=True)
    company_branch = models.ForeignKey('CompanyBranch', models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'cl_communication_log'
        verbose_name = 'Komunikacja z klientem'
        verbose_name_plural  = 'Log komunikacji z klientami'

    def __str__(self):
        return str(self.id_cl_communication_log)


class ClCommunicationReason(models.Model):
    id_client_communication_reason = models.CharField(primary_key=True, max_length=10)
    reason_name = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cl_communication_reason'
        verbose_name = "Powod komunikacji"
        verbose_name_plural = "Slownik powodow komunikacji"

    def __str__(self):
        return str(self.id_client_communication_reason)


class ClDiscount(models.Model):
    id_cl_discount = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING, db_column='client')
    discount = models.ForeignKey('DiscountDict', models.DO_NOTHING, db_column='discount')
    company_branch = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cl_discount'
        unique_together = (('client', 'discount'),)
        verbose_name = "Znizka dla klienta"
        verbose_name_plural = "Znizki dla klientow"

    def __str__(self):
        return str(self.id_cl_discount)

class ClParams(models.Model):
    max_debt = models.FloatField()
    allow_new_no_contact = models.BooleanField()
    default_reminder_sms_minutes = models.IntegerField()
    default_reminder_email_minutes = models.IntegerField()
    default_finished_info_sms = models.BooleanField()
    default_finished_info_email = models.BooleanField()
    max_worktime_wo_conf_minutes = models.IntegerField()
    default_currency = models.ForeignKey('Currrency', models.DO_NOTHING, db_column='default_currency')
    company_branch = models.ForeignKey('CompanyBranch', models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'cl_params'
        verbose_name = "Parametry modulu klienta"
        verbose_name_plural = "Parametry modulu klienta"

    def __str__(self):
        return str(self.company_branch)

class ClPayment(models.Model):
    id_cl_payment = models.AutoField(primary_key=True)
    is_closed = models.NullBooleanField()
    payment_name = models.CharField(max_length=200, blank=True, null=True)
    client = models.ForeignKey('Client', models.DO_NOTHING, db_column='client')
    is_invoice = models.NullBooleanField()
    contact = models.ForeignKey('Contact', models.DO_NOTHING, db_column='contact')
    invoice_voucher = models.CharField(unique=True, max_length=15, blank=True, null=True)
    payment_sum = models.FloatField(blank=True, null=True)
    paid_amount = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey('Currrency', models.DO_NOTHING, db_column='currency')
    paid_datetime = models.DateTimeField(blank=True, null=True)
    posted_datetime = models.DateTimeField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=400, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=10, blank=True, null=True)
    company_branch = models.ForeignKey('CompanyBranch', models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'cl_payment'
        verbose_name = 'Platnosc klienta'
        verbose_name_plural = 'Platnosci klientow'

    def __str__(self):
        return str(self.id_cl_payment)


class ClPaymentLine(models.Model):
    id_cl_payment_line = models.AutoField(primary_key=True)
    payment = models.ForeignKey(ClPayment, models.DO_NOTHING, db_column='payment')
    service = models.ForeignKey('Service', models.DO_NOTHING, db_column='service')
    text_on_invoice = models.CharField(max_length=200)
    qty = models.FloatField(blank=True, null=True)
    final_price = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey('Currrency', models.DO_NOTHING, db_column='currency')
    company_branch = models.ForeignKey('CompanyBranch', models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'cl_payment_line'
        verbose_name = 'Linia platnosci klienta'
        verbose_name_plural = 'Linie platnosci klientow'

    def __str__(self):
        return str(self.id_cl_payment_line)


class ClUnconfirmed(models.Model):
    cl_unconfirmed = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    client_name = models.CharField(max_length=200, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    default_company_branch = models.ForeignKey('CompanyBranch', models.DO_NOTHING, db_column='default_company_branch')

    class Meta:
        managed = False
        db_table = 'cl_unconfirmed'
        verbose_name = 'Niepotwierdzony klient'
        verbose_name_plural = 'Niepotwierdzeni klienci'

    def __str__(self):
        return str(self.cl_unconfirmed)


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    sex = models.ForeignKey('SexDict', models.DO_NOTHING, db_column='sex', blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    is_company = models.NullBooleanField()
    client_name = models.CharField(max_length=200, blank=True, null=True)
    nip = models.CharField(max_length=11, blank=True, null=True)
    contact = models.ForeignKey('Contact', models.DO_NOTHING, db_column='contact', blank=True, null=True)
    is_blocked = models.NullBooleanField()
    blocked_reason = models.ForeignKey(ClBlockedReasonDict, models.DO_NOTHING, blank=True, null=True)
    blocked_notes = models.CharField(max_length=400, blank=True, null=True)
    default_invoice = models.NullBooleanField()
    default_reminder_sms_minutes = models.IntegerField(blank=True, null=True)
    is_confirmed = models.NullBooleanField()
    is_rejected = models.NullBooleanField()
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    default_reminder_email_minutes = models.IntegerField(blank=True, null=True)
    default_finished_info_sms = models.IntegerField(blank=True, null=True)
    default_finished_info_email = models.IntegerField(blank=True, null=True)
    client_discount_percent_sum = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=400, blank=True, null=True)
    default_company_branch = models.ForeignKey('CompanyBranch', models.DO_NOTHING, db_column='default_company_branch')

    class Meta:
        managed = True
        db_table = 'client'
        verbose_name = 'Klinet'
        verbose_name_plural = 'Lista klientow'

    def __str__(self):
        return str("{0} {1} {2}".format(self.first_name, self.last_name, self.client_name))
        ##return 'abc'

class CompanyBranch(models.Model):
    id_company_branch = models.CharField(primary_key=True, max_length=10)
    is_main = models.NullBooleanField()
    company_name = models.CharField(max_length=200, blank=True, null=True)
    nip = models.CharField(max_length=11, blank=True, null=True)
    contact = models.ForeignKey('Contact', models.DO_NOTHING, db_column='contact')

    class Meta:
        managed = False
        db_table = 'company_branch'
        verbose_name = 'Oddzial'
        verbose_name_plural = 'Lista oddzialow'

    def __str__(self):
        return self.id_company_branch


class Contact(models.Model):
    id_contact = models.AutoField(primary_key=True)
    prefered_contact_type = models.ForeignKey('ContactType', models.DO_NOTHING, db_column='prefered_contact_type', blank=True, null=True)
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_no = models.CharField(max_length=5, blank=True, null=True)
    apartment_no = models.CharField(max_length=5, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    country = models.ForeignKey('CountryDict', models.DO_NOTHING, db_column='country', blank=True, null=True)
    notes = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'
        verbose_name = 'Kontakt'
        verbose_name_plural = 'Lista kontakow'

    def __str__(self):
        return str(self.id_contact)

class ContactType(models.Model):
    id_contact_type = models.CharField(primary_key=True, max_length=10)
    contact_type_name = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_type'
        verbose_name = 'Typ kontaktu'
        verbose_name_plural = 'Slownik typow kontaktu'

    def __str__(self):
        return str(self.id_contact_type)


class CountryDict(models.Model):
    country = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'country_dict'
        verbose_name = 'Panstwo'
        verbose_name_plural = 'Slownik panstw'

    def __str__(self):
        return self.country


class Currrency(models.Model):
    id_currency = models.CharField(primary_key=True, max_length=10)
    currency_name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    ratio_to_main_currency = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currrency'
        verbose_name = 'Waluta'
        verbose_name_plural = 'Slownik walut'


class DiscountDict(models.Model):
    id_discount_dict = models.CharField(primary_key=True, max_length=10)
    discount_name = models.CharField(max_length=100, blank=True, null=True)
    scope = models.ForeignKey('DiscountScope', models.DO_NOTHING, db_column='scope')
    discount_amount = models.FloatField(blank=True, null=True)
    discount_percent = models.FloatField(blank=True, null=True)
    valid_from = models.DateField(blank=True, null=True)
    valid_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount_dict'
        verbose_name = 'Znizka'
        verbose_name_plural = 'Slownik znizek'

    def __str__(self):
        return self.discount_name

class DiscountScope(models.Model):
    id_discount_scope = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'discount_scope'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Location(models.Model):
    id_location = models.AutoField(primary_key=True)
    location_name = models.CharField(unique=True, max_length=200, blank=True, null=True)
    location_type = models.ForeignKey('LocationType', models.DO_NOTHING, db_column='location_type')
    is_operational = models.NullBooleanField()
    notes = models.CharField(max_length=400, blank=True, null=True)
    company_branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'location'
        verbose_name = 'Lokalizacja'
        verbose_name_plural = 'Lokalizacje'

    def __str__(self):
        return self.location_name

class LocationType(models.Model):
    id_location_type = models.CharField(primary_key=True, max_length=10)
    location_type_name = models.CharField(unique=True, max_length=200, blank=True, null=True)
    location_capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_type'
        verbose_name = 'Typ lokacji'
        verbose_name_plural = 'Lista typow lokacji'

    def __str__(self):
        return self.location_type_name


class Machine(models.Model):
    id_machine = models.AutoField(primary_key=True)
    machine_name = models.CharField(max_length=200)
    machine_type = models.ForeignKey('MachineType', models.DO_NOTHING, db_column='machine_type')
    service_interval = models.IntegerField(blank=True, null=True)
    last_service = models.DateField(blank=True, null=True)
    is_operational = models.NullBooleanField()
    notes = models.CharField(max_length=400, blank=True, null=True)
    company_branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'machine'
        verbose_name = 'Maszyna'
        verbose_name_plural = 'Maszyny'

    def __str__(self):
        if self.machine_name:
            return self.machine_name
        else:
            return str(self.machine_type) + str(self.id_machine)


class MachineType(models.Model):
    id_machine_type = models.CharField(primary_key=True, max_length=10)
    machine_type_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'machine_type'
        verbose_name = 'Typ maszyny'
        verbose_name_plural = 'Typy maszyn'

    def __str__(self):
        return str(self.id_machine_type)


class ResourcesUsage(models.Model):
    id_resources_usage = models.AutoField(primary_key=True)
    service = models.ForeignKey('Service', models.DO_NOTHING, db_column='service', blank=True, null=True)
    machine = models.ForeignKey(Machine, models.DO_NOTHING, db_column='machine', blank=True, null=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker', blank=True, null=True)
    time_slot = models.ForeignKey('TimeSlotList', models.DO_NOTHING, db_column='time_slot', blank=True, null=True)
    start_timestamp = models.DateTimeField(db_column='start_timestamp')
    finish_timestamp = models.DateTimeField(db_column='finish_timestamp')
    calendar_date = models.ForeignKey('WorkdayCalendar', models.DO_NOTHING, db_column='calendar_date', blank=True, null=True)
    company_branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING, db_column='company_branch')


    class Meta:
        managed = False
        db_table = 'resources_usage'
        unique_together = (('worker', 'time_slot', 'calendar_date'), ('machine', 'time_slot', 'calendar_date'),)
        verbose_name = 'Uzycie zasobu'
        verbose_name_plural = 'Wykorzystanie zasobow'

    def __str__(self):
        return str(self.id_resources_usage)


class ResourcesUsageParams(models.Model):
    allow_using_machine_without_service_days_before_date = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'resources_usage_params'
        verbose_name = 'Parametry modulu wykorzystania zasobow'
        verbose_name_plural = 'Parametry modulu wykorzystania zasobow'

    def __str__(self):
        return 'Parametry modulu wykorzystania zasobow'


class SeDict(models.Model):
    id_se_dict = models.CharField(primary_key=True, max_length=10)
    se_dict_name = models.CharField(unique=True, max_length=200)
    base_price = models.FloatField(blank=True, null=True)
    location_type = models.ForeignKey(LocationType, models.DO_NOTHING, db_column='location_type', blank=True, null=True)
    avg_time = models.IntegerField(blank=True, null=True)
    continous = models.BooleanField()
    notes = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_dict'
        verbose_name = 'Serwis'
        verbose_name_plural = 'Slownik serwisow'

    def __str__(self):
        return str(self.id_se_dict)


class SeDiscount(models.Model):
    id_se_discount = models.AutoField(primary_key=True)
    discount = models.ForeignKey(DiscountDict, models.DO_NOTHING, db_column='discount')
    service = models.ForeignKey('Service', models.DO_NOTHING, db_column='service')
    company_branch = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'se_discount'
        verbose_name = 'Znizka na serwis'
        verbose_name_plural = 'Znizki na serwis'

    def __str__(self):
        return str(self.id_sex_dict)

class SeRequirement(models.Model):
    id_se_requirement = models.AutoField(primary_key=True)
    service_code = models.ForeignKey(SeDict, models.DO_NOTHING, db_column='service_code')
    machine_type = models.ForeignKey(MachineType, models.DO_NOTHING, db_column='machine_type', blank=True, null=True)
    worker_ability = models.ForeignKey('WoAbility', models.DO_NOTHING, db_column='worker_ability', blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    activity_sort_order = models.IntegerField(blank=True, null=True)
    activity_name = models.CharField(max_length=200, blank=True, null=True)
    time_minutes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'se_requirement'
        verbose_name = 'Wymaganie serwisu'
        verbose_name_plural = 'Wymagania serwisow'

    def __str__(self):
        return str(self.id_se_requirement)

class Service(models.Model):
    id_service = models.AutoField(primary_key=True)
    is_confirmed = models.NullBooleanField()
    service_code = models.ForeignKey(SeDict, models.DO_NOTHING, db_column='service_code')
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='location', blank=True, null=True)
    create_invoice = models.NullBooleanField()
    service_discount_amount = models.TextField(blank=True, null=True)  # This field type is a guess.
    service_discount_percent = models.FloatField(blank=True, null=True)
    min_start_datetime = models.DateTimeField(blank=True, null=True)
    planned_start = models.DateField(blank=True, null=True)
    planned_end = models.DateField(blank=True, null=True)
    real_start = models.DateField(blank=True, null=True)
    real_end = models.DateField(blank=True, null=True)
    reminder_sms_minutes = models.IntegerField(blank=True, null=True)
    reminder_email_minutes = models.IntegerField(blank=True, null=True)
    finished_info_sms = models.NullBooleanField()
    finished_info_email = models.NullBooleanField()
    notes = models.CharField(max_length=400, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=10, blank=True, null=True)
    confirmed_datetime = models.DateTimeField(blank=True, null=True)
    confirmed_by = models.CharField(max_length=10, blank=True, null=True)
    company_branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'service'
        verbose_name = 'Serwis'
        verbose_name_plural = 'Lista serwisow'

    def __str__(self):
        return str(self.id_service)


class ServiceArchived(models.Model):
    id_service_archived = models.AutoField(primary_key=True)
    id_service = models.IntegerField()
    service_code = models.CharField(max_length=10)
    service_name = models.CharField(max_length=200, blank=True, null=True)
    service_discount_amount = models.FloatField(blank=True, null=True)
    service_discount_percent = models.FloatField(blank=True, null=True)
    client = models.IntegerField()
    client_first_name = models.CharField(max_length=20, blank=True, null=True)
    client_last_name = models.CharField(max_length=20, blank=True, null=True)
    client_name = models.CharField(max_length=200, blank=True, null=True)
    client_discount = models.FloatField(blank=True, null=True)
    location = models.IntegerField(blank=True, null=True)
    location_name = models.CharField(max_length=200, blank=True, null=True)
    planned_start = models.DateField(blank=True, null=True)
    planned_end = models.DateField(blank=True, null=True)
    real_start = models.DateField(blank=True, null=True)
    real_end = models.DateField(blank=True, null=True)
    reminder_sms_minutes = models.IntegerField(blank=True, null=True)
    reminder_email_minutes = models.IntegerField(blank=True, null=True)
    finished_info_sms = models.NullBooleanField()
    finished_info_email = models.NullBooleanField()
    notes = models.CharField(max_length=400, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=10, blank=True, null=True)
    is_confirmed = models.NullBooleanField()
    confirmed_datetime = models.DateTimeField(blank=True, null=True)
    confirmed_by = models.CharField(max_length=10, blank=True, null=True)
    is_deleted = models.NullBooleanField()
    deleted_timestamp = models.DateTimeField(blank=True, null=True)
    deleted_by = models.CharField(max_length=10, blank=True, null=True)
    deleted_reason = models.CharField(max_length=400, blank=True, null=True)
    company_branch = models.CharField(max_length=10)
    min_start_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_archived'
        verbose_name = 'Serwis archiwalny'
        verbose_name_plural = 'Archiwum serwisow'

    def __str__(self):
        return str(self.id_service_archived)



class SexDict(models.Model):
    id_sex_dict = models.CharField(primary_key=True, max_length=1)
    sex = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sex_dict'
        verbose_name = 'Plec'
        verbose_name_plural = 'Slownik plci'

    def __str__(self):
        return str(self.id_sex_dict)


class TimeSlotList(models.Model):
    id_time_slot = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'time_slot_list'
        verbose_name = 'Sloty czasowe'
        verbose_name_plural = 'Sloty czasowe'

    def __str__(self):
        return str(self.id_time_slot)


class TimeSlotParams(models.Model):
    time_slot_minutes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'time_slot_params'
        verbose_name = 'Parametry slotow czasowych'
        verbose_name_plural = 'Parametry slotow czasowych'

    def __str__(self):
        return 'Parametry slotow czasowych'


class WoAbility(models.Model):
    id_wo_ability = models.AutoField(primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker')
    worker_ability = models.ForeignKey('WoAbilityDict', models.DO_NOTHING, db_column='worker_ability')
    notes = models.CharField(max_length=400, blank=True, null=True)
    company_branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'wo_ability'
        verbose_name = 'Umiejetnosc pracownika'
        verbose_name_plural = 'Umiejetnosci pracownikow'

    def __str__(self):
        return str(self.id_wo_ability)


class WoAbilityDict(models.Model):
    id_wo_ability_dict = models.CharField(primary_key=True, max_length=10)
    ability_name = models.CharField(max_length=200)
    ability_group = models.ForeignKey('WoAbilityGroupDict', models.DO_NOTHING, db_column='ability_group', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wo_ability_dict'
        verbose_name = 'Umiejetnosc'
        verbose_name_plural = 'Slownik umiejetnosci'

    def __str__(self):
        return str(self.id_wo_ability_dict)

class WoAbilityGroupDict(models.Model):
    id_wo_ablility_group_dict = models.CharField(primary_key=True, max_length=10)
    ability_group_name = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'wo_ability_group_dict'
        verbose_name = 'Grupa umiejetnosci'
        verbose_name_plural = 'Slownik grup umijetnosci'

    def __str__(self):
        return str(self.id_wo_ablility_group_dict)

class WoAbsence(models.Model):
    id_wo_absence = models.IntegerField(primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker')
    absence_type = models.ForeignKey('WoAbsenceType', models.DO_NOTHING, db_column='absence_type')
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    workdays = models.IntegerField(blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=400, blank=True, null=True)
    company_branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'wo_absence'
        verbose_name = 'Absencja pracownika'
        verbose_name_plural = 'Absencje pracownikow'

    def __str__(self):
        return str(id_wo_absence)


class WoAbsenceType(models.Model):
    id_wo_absence_type = models.CharField(primary_key=True, max_length=10)
    absence_name = models.CharField(unique=True, max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wo_absence_type'
        verbose_name = 'Absencja'
        verbose_name_plural = 'Slownik absencji'

    def __str__(self):
        return str(self.id_wo_absence_type)

class WoGroup(models.Model):
    id_wo_group = models.AutoField(primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker')
    worker_group = models.ForeignKey('WoGroupDict', models.DO_NOTHING, db_column='worker_group')
    company_branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'wo_group'
        verbose_name = 'Grupa - pracownik'
        verbose_name_plural = 'Grupy pracownikow'

    def __str__(self):
        return str(self.worker_group) + " " + str(self.worker)

class WoGroupDict(models.Model):
    id_wo_group_dict = models.CharField(primary_key=True, max_length=10)
    worker_group_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wo_group_dict'
        verbose_name = 'Grupa (nazwa slownikowa)'
        verbose_name_plural = 'Slownik grupy pracownikow'

    def __str__(self):
        return str(self.id_wo_group_dict)

class WoGroupPrivilege(models.Model):
    id_wo_group_privilege = models.AutoField(primary_key=True)
    worker_group = models.ForeignKey(WoGroupDict, models.DO_NOTHING, db_column='worker_group')
    privilege = models.ForeignKey('WoPrivilegeDict', models.DO_NOTHING)
    view_id = models.CharField(max_length=100, blank=True, null=True)
    privilege_level = models.ForeignKey('WoPrivilegeLevelDict', models.DO_NOTHING, db_column='privilege_level')

    class Meta:
        managed = False
        db_table = 'wo_group_privilege'
        unique_together = (('worker_group', 'privilege'),)
        verbose_name = 'Uprawnienie grupy'
        verbose_name_plural = 'Uprawnienia grupy'

    def __str__(self):
        return str(self.privilage) + " " + str(self.worker_group)


class WoNotification(models.Model):
    id_wo_notification = models.AutoField(primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker')
    worker_group = models.ForeignKey(WoGroupDict, models.DO_NOTHING, db_column='worker_group')
    notification_subject = models.CharField(max_length=200, blank=True, null=True)
    notification_text = models.CharField(max_length=400, blank=True, null=True)
    severity = models.IntegerField(blank=True, null=True)
    marked_as_read = models.NullBooleanField()
    company_branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'wo_notification'
        verbose_name = 'Alert pracownika'
        verbose_name_plural = 'Alerty pracownika'

    def __str__(self):
        return str(self.id_wo_notification)


class WoPrivilegeDict(models.Model):
    id_wo_privilige_dict = models.IntegerField(primary_key=True)
    privilege_name = models.CharField(unique=True, max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wo_privilege_dict'
        verbose_name = 'Uprawnienie pracownika'
        verbose_name_plural = 'Slownik uprawnien pracownikow'

    def __str__(self):
        return str(self.id_wo_privilige_dict)

class WoPrivilegeLevelDict(models.Model):
    id_wo_privilege_level_dict = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'wo_privilege_level_dict'
        verbose_name = 'Poziom uprawnienia pracownika'
        verbose_name_plural = 'Slownik poziomow uprawnien pracownika'

    def __str__(self):
        return str(self.id_sex_dict)

class WoUser(models.Model):
    app_user = models.CharField(primary_key=True, max_length=10)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker')

    class Meta:
        managed = False
        db_table = 'wo_user'
        verbose_name = 'Pracownik - user'
        verbose_name_plural = 'Relacje praconicy - userzy'

    def __str__(self):
        return self.app_user + ' ' + self.worker


class WorkdayCalendar(models.Model):
    id_workday_calendar = models.DateField(primary_key=True)
    is_workday = models.BooleanField()
    work_start = models.TimeField(blank=True, null=True)
    work_end = models.TimeField(blank=True, null=True)
    company_branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING, db_column='company_branch')

    class Meta:
        managed = False
        db_table = 'workday_calendar'
        verbose_name = 'Kaledarz roboczy'
        verbose_name_plural = 'Kalendarze robocze'

    def __str__(self):
        return str(self.company_branch)

class WorkdayCalendarParams(models.Model):
    default_workday_start_time = models.DateField(blank=True, null=True)
    default_workday_end_time = models.DateField(blank=True, null=True)
    default_saturday_start_time = models.DateField(blank=True, null=True)
    default_saturday_end_time = models.DateField(blank=True, null=True)
    default_is_saturday_workday = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'workday_calendar_params'
        verbose_name = 'Paramatry kalendarza'
        verbose_name_plural = 'Parametry kalendarza'

    def __str__(self):
        return 'nie wiem, costam'


class Worker(models.Model):
    id_worker = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    worker_title = models.CharField(max_length=200, blank=True, null=True)
    active = models.NullBooleanField()
    contact = models.ForeignKey(Contact, models.DO_NOTHING, db_column='contact', blank=True, null=True)
    notes = models.CharField(max_length=400, blank=True, null=True)
    company_branch = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'worker'
        verbose_name = 'Pracownik'
        verbose_name_plural = 'Lista pracownikow'

    def __str__(self):
        return self.last_name


class ZipCodesDict(models.Model):
    id_zip_codes_dict = models.AutoField(primary_key=True)
    country = models.ForeignKey(CountryDict, models.DO_NOTHING, db_column='country')
    zip = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_codes_dict'
        verbose_name = 'Kod pocztowy'
        verbose_name_plural = 'Slownik kodow pocztowych'

    def __str__(self):
        return self.zip
