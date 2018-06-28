# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20180613_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='alpab',
            name='date',
            field=models.DateField(verbose_name='Date', default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 20, 11, 32, 50, 977827)),
        ),
    ]
