# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 10:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speed_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speed',
            name='date',
            field=models.DateTimeField(default=datetime.timezone),
        ),
    ]