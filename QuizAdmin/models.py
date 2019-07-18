from django.db import models
from EQuiz.models import AdminUser,Organisation,Quiz
from datetime import datetime


class Questiontype(models.Model):
    Question_types = [
        ('RDB', 'Radio Buttons'),
        ('CKB', 'Check Boxes'),
        ('NUM', 'Number'),
        ('TXT', 'Text'),
    ]
    id = models.BigAutoField(db_column='ID', primary_key=True)
    description = models.CharField(
        db_column='Description', max_length=512, blank=True, null=True)
    code = models.CharField(db_column='Code', max_length=2042)
    optionsrequired = models.IntegerField(db_column='OptionsRequired')
    questionimage = models.IntegerField(
        db_column='QuestionImage', blank=True, null=True, default=0)
    answerimage = models.IntegerField(
        db_column='AnswerImage', blank=True, null=True, default=0)
    type = models.CharField(db_column='Type', max_length=3,
                            blank=True, null=True, choices=Question_types)
    madeby = models.ForeignKey(
        AdminUser, models.CASCADE, db_column='MadeBy', blank=True, null=True)
    createdon = models.DateTimeField(
        db_column='CreatedOn', blank=True, null=True)
    lastupdated = models.DateTimeField(
        db_column='LastUpdated', blank=True, null=True, editable=False, default=datetime.now())

    class Meta:
        managed = True
        db_table = 'QuestionType'
        app_label = "QuizAdmin"

    def __str__(self):
        return self.type+" "+self.description


class Question(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    question = models.CharField(db_column='Question', max_length=512)
    option1 = models.CharField(db_column='Option1', max_length=512)
    option2 = models.CharField(db_column='Option2', max_length=512)
    option3 = models.CharField(
        db_column='Option3', max_length=512, blank=True, null=True)
    option4 = models.CharField(
        db_column='Option4', max_length=512, blank=True, null=True)
    answeroption1 = models.IntegerField(db_column='AnswerOption1')
    answeroption2 = models.IntegerField(db_column='AnswerOption2')
    answeroption3 = models.IntegerField(
        db_column='AnswerOption3', blank=True, null=True)
    answeroption4 = models.IntegerField(
        db_column='AnswerOption4', blank=True, null=True)
    type = models.ForeignKey(
        'Questiontype', models.DO_NOTHING, db_column='Type')
    difficulty = models.IntegerField(db_column='Difficulty')
    attachments = models.CharField(
        db_column='Attachments', max_length=2024, blank=True, null=True)
    madeby = models.ForeignKey(
        AdminUser, models.CASCADE, db_column='MadeBy', blank=True, null=True)
    createdon = models.DateField(db_column='CreatedOn', blank=True, null=True)
    lastupdated = models.DateTimeField(
        db_column='LastUpdated', blank=True, null=True, editable=False, default=datetime.now())
    quizassociated = models.ForeignKey(
        Quiz, models.CASCADE, db_column='QuizAssociated', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Question'
        app_label = "QuizAdmin"

    def __str__(self):
        return self.id+" : "+self.question
