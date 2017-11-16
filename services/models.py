from __future__ import unicode_literals

from django.db import models

#from company.models import CompanyBranch
#from workers.models import WoAbility

class SeDict(models.Model):
    id_se_dict = models.CharField(primary_key=True, max_length=10)
    se_dict_name = models.CharField(unique=True, max_length=200)
    base_price = models.FloatField(blank=True, null=True)
    location_type = models.ForeignKey('company.LocationType', models.DO_NOTHING, db_column='location_type', blank=True, null=True)
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


#nie korzystamy
class SeDiscount(models.Model):
    id_se_discount = models.AutoField(primary_key=True)
    discount = models.ForeignKey('clients.DiscountDict', models.DO_NOTHING, db_column='discount')
    service = models.ForeignKey('Service', models.DO_NOTHING, db_column='service')
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main', related_name = '+')

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
    machine_type = models.ForeignKey('machines.MachineType', models.DO_NOTHING, db_column='machine_type', blank=True, null=True)
    worker_ability = models.ForeignKey('workers.WoAbility', models.DO_NOTHING, db_column='worker_ability', blank=True, null=True, related_name = '+')
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
    id_service = models.AutoField(primary_key=True, editable=False, verbose_name='Id')
    is_confirmed = models.NullBooleanField(default=False, verbose_name='Powierdzony')
    service_code = models.ForeignKey(SeDict, models.DO_NOTHING, db_column='service_code', verbose_name='Typ uslugi')
    client = models.ForeignKey('clients.Client', models.DO_NOTHING, db_column='client', verbose_name='Klient')
    location = models.ForeignKey('company.Location', models.DO_NOTHING, db_column='location', blank=True, null=True, verbose_name='Lokacja')
    create_invoice = models.NullBooleanField(default=False, verbose_name='Utworzyc fakture VAT')
    # TODO do ukrycia
    service_discount_amount = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10, verbose_name='Kwota znizki')
    # TODO do ukrycia
    service_discount_percent = models.FloatField(blank=True, null=True, verbose_name='Procent znizki')
    min_start_datetime = models.DateTimeField(blank=True, null=True, verbose_name='Szukanie czasu od')
    planned_start = models.DateTimeField(blank=True, null=True, verbose_name='Planowany poczatek')
    planned_end = models.DateTimeField(blank=True, null=True, verbose_name='Planowane zakonczenie')
    # TODO do ukrycia
    real_start = models.DateTimeField(blank=True, null=True, verbose_name='Rzeczywisty poczatek')
    # TODO do ukrycia
    real_end = models.DateTimeField(blank=True, null=True, verbose_name='Rzeczywiste zakonczenie')
    # TODO do ukrycia
    reminder_sms_minutes = models.IntegerField(blank=True, null=True, default=-1, verbose_name='Ilosc minut miedzy SMS a rozpoczeciem')
    # TODO do ukrycia
    reminder_email_minutes = models.IntegerField(blank=True, null=True, default=-1, verbose_name='Ilosc minut miedzy e-mail a rozpoczeciem')
    # TODO do ukrycia
    finished_info_sms = models.NullBooleanField(default=True, verbose_name='SMS o ukonczeniu')
    # TODO do ukrycia
    # test wykomnetowania pola
    finished_info_email = models.NullBooleanField(default=True, verbose_name='E-mail o ukonczeniu')
    notes = models.CharField(max_length=400, blank=True, null=True, verbose_name='Uwagi')
    # TODO do ukrycia ??
    created_datetime = models.DateTimeField(blank=True, null=True, verbose_name='Data utworzenia')
    # TODO do ukrycia
    created_by = models.CharField(max_length=10, blank=True, null=True, verbose_name='Utworzone przez')
    # TODO do ukrycia
    confirmed_datetime = models.DateTimeField(blank=True, null=True, verbose_name='Potwierdzony poczatek uslugi')
    # TODO do ukrycia
    confirmed_by = models.CharField(max_length=10, blank=True, null=True, verbose_name='Potwierdone przez')
    # TODO do ukrycia
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main', verbose_name='Oddzial', related_name = '+')

    class Meta:
        managed = False
        db_table = 'service'
        verbose_name = 'Serwis'
        verbose_name_plural = 'Lista serwisow'
        # app_label = 'Services group'

    def __str__(self):
        return 'z __str__: ' + str(self.id_service)

    def __unicode__(self):
        return 'z __unicode__: ' + str(self.id_service)


#nie korzystamy
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
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main', related_name = '+')
    min_start_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_archived'
        verbose_name = 'Serwis archiwalny'
        verbose_name_plural = 'Archiwum serwisow'

    def __str__(self):
        return str(self.id_service_archived)
