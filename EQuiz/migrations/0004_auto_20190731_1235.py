# Generated by Django 2.2.1 on 2019-07-31 07:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EQuiz', '0003_auto_20190731_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='createdon',
            field=models.DateTimeField(blank=True, db_column='CreatedOn', default=datetime.datetime(2019, 7, 31, 12, 35, 25, 539700), null=True),
        ),
    ]
