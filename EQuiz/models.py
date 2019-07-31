from django.db import models
from datetime import datetime

class Organisation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    name = models.CharField(db_column='Name', max_length=129)  
    country = models.CharField(db_column='Country', max_length=32, blank=True, null=True)  
    address = models.CharField(db_column='Address', max_length=257, blank=True, null=True)  
    representative = models.CharField(db_column='Representative', max_length=129)  
    mobile = models.CharField(db_column='Mobile', max_length=15, blank=True, null=True)  
    email = models.CharField(db_column='Email', max_length=129, blank=True, null=True)  
    type = models.CharField(db_column='Type', max_length=129)  
    createdon = models.DateField(db_column='CreatedOn', blank=True, null=True)  
    creationmode = models.CharField(db_column='CreationMode', max_length=45, default="Website",editable=False)  
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Organisation'
        app_label = "EQuiz"

class AdminUser(models.Model):
    
    name = models.CharField(db_column='UserName', unique=True, max_length=129)    
    password = models.TextField(db_column='Password')    
    organisationid = models.ForeignKey('Organisation', models.DO_NOTHING, db_column='Organisation')
    country = models.CharField(db_column='Country', max_length=33, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=257, blank=True, null=True)
    type = models.IntegerField(db_column='Type', default=1)  
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)
    creationmode = models.CharField(db_column='CreationMode', max_length=17)
    mobile = models.CharField(db_column='Mobile', max_length=13, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=129, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AdminUsers'
        app_label = "EQuiz"

    def __str__(self):
        return self.name+" : "+self.email

class Quiz(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=129)
    numberofquestions = models.IntegerField(db_column='NumberOfQuestions', blank=True)
    duration = models.BigIntegerField(db_column='Duration', blank=True, null=True)
    organisation = models.ForeignKey(Organisation, models.CASCADE, db_column='Organisation')
    positivemarks = models.IntegerField(db_column='PositiveMarks',default=1)
    negativemarks = models.IntegerField(db_column='NegativeMarks',default=0)
    description = models.CharField(db_column='Description', max_length=1025, blank=True, null=True,default='')
    difficultyratio = models.CharField(db_column='DifficultyRatio', max_length=64, blank=True, null=True,default='')
    createdby = models.ForeignKey(AdminUser, models.CASCADE, db_column='CreatedBy', blank=True, null=True)
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True,default=datetime.now())

    class Meta:
        managed = True
        db_table = 'Quiz'
        app_label = "EQuiz"