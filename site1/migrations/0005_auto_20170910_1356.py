# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0004_schedule_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='img',
            field=models.ImageField(blank=True, upload_to='static/img_schedule'),
        ),
    ]
