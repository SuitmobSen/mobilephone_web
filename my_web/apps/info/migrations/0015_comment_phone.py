# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-21 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0014_auto_20190821_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='对应机型'),
        ),
    ]
