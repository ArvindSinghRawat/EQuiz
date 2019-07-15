from django.db import models


class Adminusers(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=129)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    organisationid = models.ForeignKey('Organisation', models.DO_NOTHING, db_column='OrganisationId')  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=33, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=257, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    creationmode = models.CharField(db_column='CreationMode', max_length=17)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=13, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=129, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdminUsers'


class Organisation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=129)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=32, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=257, blank=True, null=True)  # Field name made lowercase.
    representative = models.CharField(db_column='Representative', max_length=129)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=129, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=129)  # Field name made lowercase.
    createdon = models.DateField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    creationmode = models.CharField(db_column='CreationMode', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organisation'


class Question(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=512)  # Field name made lowercase.
    option1 = models.CharField(db_column='Option1', max_length=512)  # Field name made lowercase.
    option2 = models.CharField(db_column='Option2', max_length=512)  # Field name made lowercase.
    option3 = models.CharField(db_column='Option3', max_length=512, blank=True, null=True)  # Field name made lowercase.
    option4 = models.CharField(db_column='Option4', max_length=512, blank=True, null=True)  # Field name made lowercase.
    answeroption1 = models.IntegerField(db_column='AnswerOption1')  # Field name made lowercase.
    answeroption2 = models.IntegerField(db_column='AnswerOption2')  # Field name made lowercase.
    answeroption3 = models.IntegerField(db_column='AnswerOption3', blank=True, null=True)  # Field name made lowercase.
    answeroption4 = models.IntegerField(db_column='AnswerOption4', blank=True, null=True)  # Field name made lowercase.
    type = models.ForeignKey('Questiontype', models.DO_NOTHING, db_column='Type')  # Field name made lowercase.
    difficulty = models.IntegerField(db_column='Difficulty')  # Field name made lowercase.
    attachments = models.CharField(db_column='Attachments', max_length=2024, blank=True, null=True)  # Field name made lowercase.
    madeby = models.ForeignKey(Adminusers, models.DO_NOTHING, db_column='MadeBy', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Question'


class Questiontype(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=2042)  # Field name made lowercase.
    optionsrequired = models.IntegerField(db_column='OptionsRequired')  # Field name made lowercase.
    questionimage = models.IntegerField(db_column='QuestionImage', blank=True, null=True)  # Field name made lowercase.
    answerimage = models.IntegerField(db_column='AnswerImage', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=3, blank=True, null=True)  # Field name made lowercase.
    madeby = models.ForeignKey(Adminusers, models.DO_NOTHING, db_column='MadeBy', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuestionType'


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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    mobile = models.CharField(max_length=13)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
