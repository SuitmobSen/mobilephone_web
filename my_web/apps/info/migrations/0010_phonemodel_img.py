# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-20 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_auto_20190820_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonemodel',
            name='img',
            field=models.ImageField(default='phones/default.jpg', upload_to='media/phones/', verbose_name='手机缩略图'),
        ),
    ]