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
    TF = [
        (0,'False'),
        (1,'True'),
    ]
    id = models.BigAutoField(db_column='ID', primary_key=True)
    description = models.CharField(db_column='Description', max_length=256)
    containercode = models.CharField(db_column='ContainerCode', max_length=256)
    questioncontainer = models.CharField(
        db_column='QuestionContainer', max_length=256)
    optionscontainer = models.CharField(
        db_column='OptionsContainer', max_length=256)
    questiontext = models.CharField(
        db_column='QuestionText', max_length=512, blank=True, null=True)
    questionimage = models.CharField(
        db_column='QuestionImage', max_length=512, blank=True, null=True)
    optionstext = models.CharField(
        db_column='OptionsText', max_length=512, blank=True, null=True)
    optionsimage = models.CharField(
        db_column='OptionsImage', max_length=512, blank=True, null=True)
    type = models.CharField(
        db_column='Type', max_length=3, choices=Question_types)
    imagequestion = models.IntegerField(db_column='ImageQuestion', choices=TF)
    imageoptions = models.IntegerField(
        db_column='ImageOptions', choices=TF)
    madeby = models.ForeignKey(
        AdminUser, models.CASCADE, db_column='MadeBy')
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


class QuizQuestion(models.Model):
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
    questionimage = models.ImageField(
        db_column='QuestionImage', upload_to='media/Users/', blank=True, null=True, default='')
    answerimage1 = models.ImageField(
        db_column='AnswerImage1', upload_to='media/Users/', blank=True, null=True, default='')
    answerimage2 = models.ImageField(
        db_column='AnswerImage2', upload_to='media/Users/', blank=True, null=True, default='')
    answerimage3 = models.ImageField(
        db_column='AnswerImage3', upload_to='media/Users/', blank=True, null=True, default='')
    answerimage4 = models.ImageField(
        db_column='AnswerImage4', upload_to='media/Users/', blank=True, null=True, default='')
    type = models.ForeignKey(
        Questiontype, models.DO_NOTHING, db_column='Type')
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
        db_table = 'QuizQuestion'
        app_label = "QuizAdmin"

    def __str__(self):
        return str(self.id)+" : "+str(self.question)
