# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-12 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20190812_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic',
            name='phone_type',
            field=models.TextField(default='', verbose_name='手机类型'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basic',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5, verbose_name='电商报价'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='phonemodel',
            name='basic',
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='basic',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='info.Basic', verbose_name='基本参数'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='phonemodel',
            name='screen',
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='screen',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='info.Screen', verbose_name='屏幕'),
            preserve_default=False,
        ),
    ]
