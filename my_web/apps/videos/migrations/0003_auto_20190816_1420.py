# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-16 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20190815_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videolist',
            name='tag',
            field=models.ManyToManyField(blank=True, to='videos.Tag', verbose_name='视频标签'),
        ),
    ]
