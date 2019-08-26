# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-21 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_auto_20190821_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonemodel',
            name='jd_url',
            field=models.CharField(default='https://www.jd.com', max_length=100, verbose_name='京东入口'),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='score',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.Comment', verbose_name='网友评分'),
        ),
    ]