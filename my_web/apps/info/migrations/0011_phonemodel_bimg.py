# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-20 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_phonemodel_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonemodel',
            name='bimg',
            field=models.ImageField(default='phone_img/default.jpg', upload_to='media/phone_img/', verbose_name='展示图'),
        ),
    ]