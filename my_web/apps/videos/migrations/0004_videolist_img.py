# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-16 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20190816_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='videolist',
            name='img',
            field=models.ImageField(default='video/default_300x300.jpg', upload_to='video/', verbose_name='视频缩略图'),
        ),
    ]