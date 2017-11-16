from django.db import models

#from services.models import Service
#from company.models import CompanyBranch
#from utilities.models import Currency, Address, SexDict

# Create your models here.




#nie korzystamy
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


#nie korzystamy
class ClCommunicationLog(models.Model):
    id_cl_communication_log = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING, db_column='client', blank=True, null=True)
    communication_reason = models.ForeignKey('ClCommunicationReason', models.DO_NOTHING, db_column='communication_reason', blank=True, null=True)
    service = models.ForeignKey('services.Service', models.DO_NOTHING, db_column='service', blank=True, null=True, related_name = '+')
    contact_type = models.ForeignKey('utilities.ContactType', models.DO_NOTHING, db_column='contact_type')
    contact_address = models.CharField(max_length=100, blank=True, null=True)
    message_body = models.TextField(blank=True, null=True)
    minutes_before_action = models.IntegerField(blank=True, null=True)
    notes = models.IntegerField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=10, blank=True, null=True)
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main', related_name = '+')

    class Meta:
        managed = False
        db_table = 'cl_communication_log'
        verbose_name = 'Komunikacja z klientem'
        verbose_name_plural  = 'Log komunikacji z klientami'

    def __str__(self):
        return str(self.id_cl_communication_log)


#nie korzystamy
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


#nie korzystamy
class ClDiscount(models.Model):
    id_cl_discount = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', models.DO_NOTHING, db_column='client')
    discount = models.ForeignKey('DiscountDict', models.DO_NOTHING, db_column='discount')
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main', related_name = '+')

    class Meta:
        managed = False
        db_table = 'cl_discount'
        unique_together = (('client', 'discount'),)
        verbose_name = "Znizka dla klienta"
        verbose_name_plural = "Znizki dla klientow"

    def __str__(self):
        return str(self.id_cl_discount)


class ClParams(models.Model):
    id_cl_params = models.AutoField(db_column='cl_params_id', primary_key=True)
    max_debt = models.FloatField()
    allow_new_no_contact = models.BooleanField()
    default_reminder_sms_minutes = models.IntegerField()
    default_reminder_email_minutes = models.IntegerField()
    default_finished_info_sms = models.BooleanField()
    default_finished_info_email = models.BooleanField()
    max_worktime_wo_conf_minutes = models.IntegerField()
    default_currency = models.ForeignKey('utilities.Currrency', models.DO_NOTHING, db_column='default_currency', related_name = '+')
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main', related_name = '+')

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
    address = models.ForeignKey('utilities.Address', models.DO_NOTHING, db_column='address', related_name = '+')
    invoice_voucher = models.CharField(unique=True, max_length=15, blank=True, null=True)
    payment_sum = models.FloatField(blank=True, null=True)
    paid_amount = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey('utilities.Currrency', models.DO_NOTHING, db_column='currency', related_name = '+')
    paid_datetime = models.DateTimeField(blank=True, null=True)
    posted_datetime = models.DateTimeField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=400, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=10, blank=True, null=True)
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main', related_name = '+')

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
    service = models.ForeignKey('services.Service', models.DO_NOTHING, db_column='service', related_name = '+')
    text_on_invoice = models.CharField(max_length=200)
    qty = models.FloatField(blank=True, null=True)
    final_price = models.FloatField(blank=True, null=True)
    currency = models.ForeignKey('utilities.Currrency', models.DO_NOTHING, db_column='currency', related_name = '+')
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main', related_name = '+')

    class Meta:
        managed = False
        db_table = 'cl_payment_line'
        verbose_name = 'Linia platnosci klienta'
        verbose_name_plural = 'Linie platnosci klientow'

    def __str__(self):
        return str(self.id_cl_payment_line)


#nie korzystamy
class ClUnconfirmed(models.Model):
    cl_unconfirmed = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    client_name = models.CharField(max_length=200, blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    default_company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='default_company_branch', related_name = '+')

    class Meta:
        managed = False
        db_table = 'cl_unconfirmed'
        verbose_name = 'Niepotwierdzony klient'
        verbose_name_plural = 'Niepotwierdzeni klienci'

    def __str__(self):
        return str(self.cl_unconfirmed)


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    sex = models.ForeignKey('utilities.SexDict', models.DO_NOTHING, db_column='sex', blank=True, null=True, related_name = '+')
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    is_company = models.NullBooleanField(default=False)
    client_name = models.CharField(max_length=200, blank=True, null=True)
    nip = models.CharField(max_length=11, blank=True, null=True)
    address = models.ForeignKey('utilities.Address', models.DO_NOTHING, db_column='address', blank=True, null=True, related_name = '+')
    is_blocked = models.NullBooleanField(default=False)
    # TODO schowac w adminie
    blocked_reason = models.ForeignKey(ClBlockedReasonDict, models.DO_NOTHING, blank=True, null=True)
    # TODO schowac w adminie
    blocked_notes = models.CharField(max_length=400, blank=True, null=True)
    # TODO schowac w adminie ???
    default_invoice = models.NullBooleanField(default=True)
    # TODO schowac w adminie
    default_reminder_sms_minutes = models.IntegerField(blank=True, null=True)
    is_confirmed = models.NullBooleanField(default=True)
    # TODO schowac w adminie
    is_rejected = models.NullBooleanField(default=False)
    # TODO schowac w adminie
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    # TODO schowac w adminie
    default_reminder_email_minutes = models.IntegerField(blank=True, null=True)
    # TODO schowac w adminie
    default_finished_info_sms = models.IntegerField(blank=True, null=True)
    # TODO schowac w adminie
    default_finished_info_email = models.IntegerField(blank=True, null=True)
    # TODO schowac w adminie
    client_discount_percent_sum = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=400, blank=True, null=True)
    default_company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='default_company_branch', default='main', related_name = '+')

    class Meta:
        managed = False
        db_table = 'client'
        verbose_name = 'Klinet'
        verbose_name_plural = 'Lista klientow'

    def __str__(self):
        return str("{0} {1} {2}".format(self.first_name, self.last_name, self.client_name))
        ##return 'abc'


#nie korzystamy
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


#nie korzystamy
class DiscountScope(models.Model):
    id_discount_scope = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'discount_scope'
