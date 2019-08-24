# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-14 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20190812_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='params',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='phone', to='info.Params', verbose_name='手机详细参数'),
        ),
    ]
