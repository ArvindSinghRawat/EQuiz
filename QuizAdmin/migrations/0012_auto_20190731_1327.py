# Generated by Django 2.2.1 on 2019-07-31 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizAdmin', '0011_auto_20190731_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='lastupdated',
            field=models.DateTimeField(blank=True, db_column='LastUpdated', default=datetime.datetime(2019, 7, 31, 13, 27, 47, 184027), editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='questiontype',
            name='lastupdated',
            field=models.DateTimeField(blank=True, db_column='LastUpdated', default=datetime.datetime(2019, 7, 31, 13, 27, 47, 182020), editable=False, null=True),
        ),
    ]
