# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0002_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='show_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
