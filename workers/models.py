from django.db import models

# Create your models here.

class WoAbility(models.Model):
    id_wo_ability = models.AutoField(primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker')
    worker_ability = models.ForeignKey('WoAbilityDict', models.DO_NOTHING, db_column='worker_ability')
    notes = models.CharField(max_length=400, blank=True, null=True)
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main')

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


#nie korzystamy
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


#nie korzystamy
class WoAbsence(models.Model):
    id_wo_absence = models.IntegerField(primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker')
    absence_type = models.ForeignKey('WoAbsenceType', models.DO_NOTHING, db_column='absence_type')
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    workdays = models.IntegerField(blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    notes = models.CharField(max_length=400, blank=True, null=True)
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main')

    class Meta:
        managed = False
        db_table = 'wo_absence'
        verbose_name = 'Absencja pracownika'
        verbose_name_plural = 'Absencje pracownikow'

    def __str__(self):
        return str(id_wo_absence)


#nie korzystamy
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


#nie korzystamy
class WoGroup(models.Model):
    id_wo_group = models.AutoField(primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker')
    worker_group = models.ForeignKey('WoGroupDict', models.DO_NOTHING, db_column='worker_group')
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main')

    class Meta:
        managed = False
        db_table = 'wo_group'
        verbose_name = 'Grupa - pracownik'
        verbose_name_plural = 'Grupy pracownikow'

    def __str__(self):
        return str(self.worker_group) + " " + str(self.worker)


#nie korzystamy
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


#nie korzystamy
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


#nie korzystamy
class WoNotification(models.Model):
    id_wo_notification = models.AutoField(primary_key=True)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker')
    worker_group = models.ForeignKey(WoGroupDict, models.DO_NOTHING, db_column='worker_group')
    notification_subject = models.CharField(max_length=200, blank=True, null=True)
    notification_text = models.CharField(max_length=400, blank=True, null=True)
    severity = models.IntegerField(blank=True, null=True)
    marked_as_read = models.NullBooleanField()
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main')

    class Meta:
        managed = False
        db_table = 'wo_notification'
        verbose_name = 'Alert pracownika'
        verbose_name_plural = 'Alerty pracownika'

    def __str__(self):
        return str(self.id_wo_notification)


#nie korzystamy
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


#nie korzystamy
class WoPrivilegeLevelDict(models.Model):
    id_wo_privilege_level_dict = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'wo_privilege_level_dict'
        verbose_name = 'Poziom uprawnienia pracownika'
        verbose_name_plural = 'Slownik poziomow uprawnien pracownika'

    def __str__(self):
        return str(self.id_sex_dict)


#nie korzystamy
class WoUser(models.Model):
    app_user = models.CharField(primary_key=True, max_length=10)
    worker = models.ForeignKey('Worker', models.DO_NOTHING, db_column='worker')

    class Meta:
        managed = False
        db_table = 'wo_user'
        verbose_name = 'Pracownik - user'
        verbose_name_plural = 'Relacje pracownicy - userzy'

    def __str__(self):
        return self.app_user + ' ' + self.worker





class Worker(models.Model):
    id_worker = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    worker_title = models.CharField(max_length=200, blank=True, null=True)
    active = models.NullBooleanField(default=True)
    address = models.ForeignKey('utilities.Address', models.DO_NOTHING, db_column='address', blank=True, null=True)
    notes = models.CharField(max_length=400, blank=True, null=True)
    company_branch = models.ForeignKey('company.CompanyBranch', models.DO_NOTHING, db_column='company_branch', default='main')

    class Meta:
        managed = False
        db_table = 'worker'
        verbose_name = 'Pracownik'
        verbose_name_plural = 'Lista pracownikow'

    def __str__(self):
        return self.last_name
