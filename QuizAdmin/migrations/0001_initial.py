# Generated by Django 2.2.1 on 2019-07-31 07:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EQuiz', '0002_auto_20190731_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questiontype',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='Description', max_length=256)),
                ('containercode', models.CharField(db_column='ContainerCode', max_length=256)),
                ('questioncontainer', models.CharField(db_column='QuestionContainer', max_length=256)),
                ('optionscontainer', models.CharField(db_column='OptionsContainer', max_length=256)),
                ('questiontext', models.CharField(blank=True, db_column='QuestionText', max_length=512, null=True)),
                ('questionimage', models.CharField(blank=True, db_column='QuestionImage', max_length=512, null=True)),
                ('optionstext', models.CharField(blank=True, db_column='OptionsText', max_length=512, null=True)),
                ('optionsimage', models.CharField(blank=True, db_column='OptionsImage', max_length=512, null=True)),
                ('type', models.CharField(choices=[('RDB', 'Radio Buttons'), ('CKB', 'Check Boxes'), ('NUM', 'Number'), ('TXT', 'Text')], db_column='Type', max_length=3)),
                ('imagequestion', models.IntegerField(choices=[(0, 'False'), (1, 'True')], db_column='ImageQuestion')),
                ('imageoptions', models.IntegerField(choices=[(0, 'False'), (1, 'True')], db_column='ImageOptions')),
                ('createdon', models.DateTimeField(blank=True, db_column='CreatedOn', null=True)),
                ('lastupdated', models.DateTimeField(blank=True, db_column='LastUpdated', default=datetime.datetime(2019, 7, 31, 12, 31, 1, 430764), editable=False, null=True)),
                ('madeby', models.ForeignKey(db_column='MadeBy', on_delete=django.db.models.deletion.CASCADE, to='EQuiz.AdminUser')),
            ],
            options={
                'db_table': 'QuestionType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('question', models.CharField(db_column='Question', max_length=512)),
                ('option1', models.CharField(db_column='Option1', max_length=512)),
                ('option2', models.CharField(db_column='Option2', max_length=512)),
                ('option3', models.CharField(blank=True, db_column='Option3', max_length=512, null=True)),
                ('option4', models.CharField(blank=True, db_column='Option4', max_length=512, null=True)),
                ('answeroption1', models.IntegerField(db_column='AnswerOption1')),
                ('answeroption2', models.IntegerField(db_column='AnswerOption2')),
                ('answeroption3', models.IntegerField(blank=True, db_column='AnswerOption3', null=True)),
                ('answeroption4', models.IntegerField(blank=True, db_column='AnswerOption4', null=True)),
                ('questionimage', models.ImageField(blank=True, db_column='QuestionImage', default='', null=True, upload_to='media/Users/')),
                ('answerimage1', models.ImageField(blank=True, db_column='AnswerImage1', default='', null=True, upload_to='media/Users/')),
                ('answerimage2', models.ImageField(blank=True, db_column='AnswerImage2', default='', null=True, upload_to='media/Users/')),
                ('answerimage3', models.ImageField(blank=True, db_column='AnswerImage3', default='', null=True, upload_to='media/Users/')),
                ('answerimage4', models.ImageField(blank=True, db_column='AnswerImage4', default='', null=True, upload_to='media/Users/')),
                ('difficulty', models.IntegerField(db_column='Difficulty')),
                ('attachments', models.CharField(blank=True, db_column='Attachments', max_length=2024, null=True)),
                ('createdon', models.DateField(blank=True, db_column='CreatedOn', null=True)),
                ('lastupdated', models.DateTimeField(blank=True, db_column='LastUpdated', default=datetime.datetime(2019, 7, 31, 12, 31, 1, 433755), editable=False, null=True)),
                ('madeby', models.ForeignKey(blank=True, db_column='MadeBy', null=True, on_delete=django.db.models.deletion.CASCADE, to='EQuiz.AdminUser')),
                ('quizassociated', models.ForeignKey(blank=True, db_column='QuizAssociated', null=True, on_delete=django.db.models.deletion.CASCADE, to='EQuiz.Quiz')),
                ('type', models.ForeignKey(db_column='Type', on_delete=django.db.models.deletion.DO_NOTHING, to='QuizAdmin.Questiontype')),
            ],
            options={
                'db_table': 'Question',
                'managed': True,
            },
        ),
    ]