# Generated by Django 2.2.1 on 2019-07-31 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizAdmin', '0005_auto_20190731_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='lastupdated',
            field=models.DateTimeField(blank=True, db_column='LastUpdated', default=datetime.datetime(2019, 7, 31, 13, 24, 16, 901896), editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='questiontype',
            name='lastupdated',
            field=models.DateTimeField(blank=True, db_column='LastUpdated', default=datetime.datetime(2019, 7, 31, 13, 24, 16, 899901), editable=False, null=True),
        ),
    ]
