# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-18 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newslist',
            options={'verbose_name': '机情快讯列表', 'verbose_name_plural': '机情快讯列表'},
        ),
    ]
