# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


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

class AdminUser(models.Model):
    
    name = models.CharField(db_column='UserName', unique=True, max_length=129)
    
    password = models.TextField(db_column='Password')
    
    organisationid = models.ForeignKey(
        'Organisation', models.DO_NOTHING, db_column='Organisation')
    
    country = models.CharField(
        db_column='Country', max_length=33, blank=True, null=True)
    
    address = models.CharField(
        db_column='Address', max_length=257, blank=True, null=True)
    type = models.IntegerField(db_column='Type', default=1)  
    
    createdon = models.DateTimeField(
        db_column='CreatedOn', blank=True, null=True)
    
    creationmode = models.CharField(db_column='CreationMode', max_length=17)
    
    mobile = models.CharField(
        db_column='Mobile', max_length=13, blank=True, null=True)
    
    email = models.CharField(
        db_column='Email', max_length=129, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AdminUsers'

    def __str__(self):
        return self.name+" : "+self.email

class Question(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  
    question = models.CharField(db_column='Question', max_length=512)  
    option1 = models.CharField(db_column='Option1', max_length=512)  
    option2 = models.CharField(db_column='Option2', max_length=512)  
    option3 = models.CharField(db_column='Option3', max_length=512, blank=True, null=True)  
    option4 = models.CharField(db_column='Option4', max_length=512, blank=True, null=True)  
    answeroption1 = models.IntegerField(db_column='AnswerOption1')  
    answeroption2 = models.IntegerField(db_column='AnswerOption2')  
    answeroption3 = models.IntegerField(db_column='AnswerOption3', blank=True, null=True)  
    answeroption4 = models.IntegerField(db_column='AnswerOption4', blank=True, null=True)  
    type = models.ForeignKey('Questiontype', models.DO_NOTHING, db_column='Type')  
    difficulty = models.IntegerField(db_column='Difficulty')  
    attachments = models.CharField(db_column='Attachments', max_length=2024, blank=True, null=True)  
    madeby = models.ForeignKey('AdminUser', models.CASCADE, db_column='MadeBy', blank=True, null=True)  
    createdon = models.DateField(db_column='CreatedOn', blank=True, null=True)  
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True,editable=False,default=datetime.now()) 
    quizassociated = models.ForeignKey('Quiz', models.CASCADE, db_column='QuizAssociated', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Question'

    def __str__(self):
        return self.id+" : "+self.question

class Questiontype(models.Model):
    Question_types = [
        ('RDB', 'Radio Buttons'),
        ('CKB', 'Check Boxes'),
        ('NUM', 'Number'),
        ('TXT', 'Text'),
    ]
    id = models.BigAutoField(db_column='ID', primary_key=True)  
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  
    code = models.CharField(db_column='Code', max_length=2042)  
    optionsrequired = models.IntegerField(db_column='OptionsRequired')  
    questionimage = models.IntegerField(db_column='QuestionImage', blank=True, null=True,default=0)  
    answerimage = models.IntegerField(db_column='AnswerImage', blank=True, null=True,default=0)  
    type = models.CharField(db_column='Type', max_length=3, blank=True, null=True,choices=Question_types)  
    madeby = models.ForeignKey('AdminUser', models.CASCADE, db_column='MadeBy', blank=True, null=True)  
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True,editable=False,default=datetime.now())  

    class Meta:
        managed = True
        db_table = 'QuestionType'

    def __str__(self):
        return self.type+" "+self.description

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
    createdby = models.ForeignKey('AdminUser', models.CASCADE, db_column='CreatedBy', blank=True, null=True)
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True,default=datetime.now())

    class Meta:
        managed = True
        db_table = 'Quiz'
