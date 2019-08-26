# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-21 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_phonemodel_bimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xjb', models.CharField(max_length=5, verbose_name='性价比')),
                ('xn', models.CharField(max_length=5, verbose_name='性能')),
                ('xh', models.CharField(max_length=5, verbose_name='续航')),
                ('wg', models.CharField(max_length=5, verbose_name='外观')),
                ('pz', models.CharField(max_length=5, verbose_name='拍照')),
            ],
            options={
                'verbose_name': 'ZOL网友评分表',
                'verbose_name_plural': 'ZOL网友评分表',
            },
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='jd_goodrate',
            field=models.CharField(default='暂无数据', max_length=10, verbose_name='京东好评率'),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='jd_price',
            field=models.CharField(default='暂无报价', max_length=10, verbose_name='京东报价'),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='sn_goodrate',
            field=models.CharField(default='暂无数据', max_length=10, verbose_name='苏宁好评率'),
        ),
    ]