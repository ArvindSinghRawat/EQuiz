# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.db import models


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
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Organisation'
        
class AdminUsers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=129)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=129)  # Field name made lowercase.
    organisationid = models.ForeignKey('Organisation', models.CASCADE, db_column='OrganisationId')  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=33, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=257, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    creationmode = models.CharField(db_column='CreationMode', max_length=17)  # Field name made lowercase.
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'AdminUsers'

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
    type = models.ForeignKey('Questiontype', models.CASCADE, db_column='Type')  # Field name made lowercase.
    madeby = models.ForeignKey('AdminUsers', models.CASCADE, db_column='MadeBy', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.
    attachments = models.CharField(db_column='Attachments', max_length=2024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Question'


class Questiontype(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=2042)  # Field name made lowercase.
    optionsrequired = models.IntegerField(db_column='OptionsRequired')  # Field name made lowercase.
    madeby = models.CharField(db_column='MadeBy', max_length=129, blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'QuestionType'