from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CptInfo(models.Model):
    cpt_id = models.IntegerField(primary_key=True)
    ide_id = models.IntegerField(blank=True, null=True)
    cp_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cpt_info'


class Crup(models.Model):
    operate_id = models.IntegerField(blank=True, null=True)
    operate_name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'crup'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserAdmin', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DpttInfo(models.Model):
    bumen_biao = models.IntegerField()
    cp_biao = models.ForeignKey(CptInfo, models.DO_NOTHING, db_column='cp_biao', blank=True, null=True)
    dptt = models.IntegerField()
    dptt_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dptt_info'


class ModuleDefine(models.Model):
    modle_id = models.AutoField(primary_key=True)
    modle_name = models.CharField(max_length=64, blank=True, null=True)
    modle_parent = models.IntegerField(blank=True, null=True)
    models_key =models.ForeignKey('ModuleDefine',models.CASCADE)
    modle_hierarchy = models.CharField(max_length=255, blank=True, null=True)
    modle_level = models.SmallIntegerField(blank=True, null=True)
    icon_name = models.CharField(max_length=255, blank=True, null=True)
    module_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'module_define'


class PormissionDefine(models.Model):
    role = models.ForeignKey('RoleDefine', models.DO_NOTHING, primary_key=True)
    module = models.ForeignKey(ModuleDefine, models.DO_NOTHING, blank=True, null=True)
    crud_opreation = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pormission_define'


class RoleDefine(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=20, blank=True, null=True)
    role_description = models.CharField(max_length=256, blank=True, null=True)
    role_priv_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'role_define'


class StallInfo(models.Model):
    staff_ide = models.IntegerField(blank=True, null=True)
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=6)
    com_ide = models.ForeignKey(CptInfo, models.DO_NOTHING, db_column='com_ide', blank=True, null=True)
    department = models.ForeignKey(DpttInfo, models.DO_NOTHING, db_column='department', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stall_info'


class UserAdmin(AbstractUser):
    name = models.CharField(max_length=20, blank=True, null=True)
    pwd = models.CharField(max_length=32, blank=True, null=True)
    role_priv_level = models.CharField(max_length=11, blank=True, null=True)
    role = models.ForeignKey(RoleDefine, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(CptInfo, models.DO_NOTHING, blank=True, null=True)
    dept = models.ForeignKey(DpttInfo, models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(StallInfo, models.DO_NOTHING, blank=True, null=True)
    if_online = models.IntegerField(blank=True, null=True)
    is_locked = models.IntegerField(blank=True, null=True)
    user_espired = models.DateTimeField(blank=True, null=True)
    user_modile = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_admin'
