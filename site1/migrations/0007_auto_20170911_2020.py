# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0006_auto_20170910_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='img',
            field=models.ImageField(blank=True, upload_to='site1/static/img_schedule'),
        ),
    ]
