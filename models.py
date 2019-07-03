# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adminusers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=129)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=129)  # Field name made lowercase.
    organisationid = models.ForeignKey('Organisation', models.DO_NOTHING, db_column='OrganisationId')  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=33, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=257, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    creationmode = models.CharField(db_column='CreationMode', max_length=17)  # Field name made lowercase.

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
