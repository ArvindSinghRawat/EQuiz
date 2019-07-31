# Generated by Django 2.2.1 on 2019-07-31 07:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EQuiz', '0006_auto_20190731_1325'),
        ('QuizAdmin', '0006_auto_20190731_1324'),
    ]

    operations = [
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
                ('lastupdated', models.DateTimeField(blank=True, db_column='LastUpdated', default=datetime.datetime(2019, 7, 31, 13, 25, 22, 543384), editable=False, null=True)),
                ('madeby', models.ForeignKey(blank=True, db_column='MadeBy', null=True, on_delete=django.db.models.deletion.CASCADE, to='EQuiz.AdminUser')),
                ('quizassociated', models.ForeignKey(blank=True, db_column='QuizAssociated', null=True, on_delete=django.db.models.deletion.CASCADE, to='EQuiz.Quiz')),
            ],
            options={
                'db_table': 'QuizQuestion',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='questiontype',
            name='lastupdated',
            field=models.DateTimeField(blank=True, db_column='LastUpdated', default=datetime.datetime(2019, 7, 31, 13, 25, 22, 541385), editable=False, null=True),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='type',
            field=models.ForeignKey(db_column='Type', on_delete=django.db.models.deletion.DO_NOTHING, to='QuizAdmin.Questiontype'),
        ),
    ]
