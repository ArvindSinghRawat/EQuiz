# Generated by Django 2.2.1 on 2019-07-14 16:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=129)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=32, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=257, null=True)),
                ('representative', models.CharField(db_column='Representative', max_length=129)),
                ('mobile', models.CharField(blank=True, db_column='Mobile', max_length=15, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=129, null=True)),
                ('type', models.CharField(db_column='Type', max_length=129)),
                ('createdon', models.DateField(blank=True, db_column='CreatedOn', null=True)),
                ('creationmode', models.CharField(blank=True, db_column='CreationMode', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Organisation',
            },
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=129, unique=True)),
                ('password', models.CharField(db_column='Password', max_length=129)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=33, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=257, null=True)),
                ('type', models.IntegerField(db_column='Type')),
                ('createdon', models.DateTimeField(blank=True, db_column='CreatedOn', null=True)),
                ('creationmode', models.CharField(db_column='CreationMode', default='Website', max_length=17)),
                ('mobile', models.CharField(blank=True, db_column='Mobile', max_length=13, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=129, null=True)),
                ('organisationid', models.ForeignKey(db_column='OrganisationId', on_delete=django.db.models.deletion.CASCADE, to='EQuiz.Organisation')),
            ],
            options={
                'db_table': 'AdminUsers',
            },
        ),
        migrations.CreateModel(
            name='Questiontype',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=512, null=True)),
                ('code', models.CharField(db_column='Code', max_length=2042)),
                ('optionsrequired', models.IntegerField(db_column='OptionsRequired')),
                ('questionimage', models.IntegerField(blank=True, db_column='QuestionImage', default=0, null=True)),
                ('answerimage', models.IntegerField(blank=True, db_column='AnswerImage', default=0, null=True)),
                ('type', models.CharField(blank=True, choices=[('RDB', 'Radio Buttons'), ('CKB', 'Check Boxes'), ('NUM', 'Number'), ('TXT', 'Text')], db_column='Type', max_length=3, null=True)),
                ('createdon', models.DateTimeField(blank=True, db_column='CreatedOn', null=True)),
                ('lastupdated', models.DateTimeField(blank=True, db_column='LastUpdated', default=datetime.datetime(2019, 7, 14, 21, 56, 38, 1652), editable=False, null=True)),
                ('madeby', models.ForeignKey(blank=True, db_column='MadeBy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'QuestionType',
            },
        ),
        migrations.CreateModel(
            name='Question',
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
                ('difficulty', models.IntegerField(db_column='Difficulty')),
                ('attachments', models.CharField(blank=True, db_column='Attachments', max_length=2024, null=True)),
                ('createdon', models.DateField(blank=True, db_column='CreatedOn', null=True)),
                ('lastupdated', models.DateTimeField(blank=True, db_column='LastUpdated', default=datetime.datetime(2019, 7, 14, 21, 56, 38, 651), editable=False, null=True)),
                ('madeby', models.ForeignKey(blank=True, db_column='MadeBy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(db_column='Type', on_delete=django.db.models.deletion.DO_NOTHING, to='EQuiz.Questiontype')),
            ],
            options={
                'db_table': 'Question',
            },
        ),
    ]
