# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_partecipants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alpab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('charr', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 13, 15, 3, 20, 331323)),
        ),
    ]
