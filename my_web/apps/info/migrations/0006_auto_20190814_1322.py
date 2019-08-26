# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-14 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20190814_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.CharField(blank=True, max_length=50, verbose_name='CPU')),
                ('back', models.CharField(blank=True, max_length=50, verbose_name='后置')),
                ('front', models.CharField(blank=True, max_length=50, verbose_name='前置')),
                ('memory', models.CharField(blank=True, max_length=50, verbose_name='内存')),
                ('battery', models.CharField(blank=True, max_length=50, verbose_name='电池')),
                ('screen', models.CharField(blank=True, max_length=50, verbose_name='屏幕')),
                ('dpi', models.CharField(blank=True, max_length=50, verbose_name='分辨率')),
            ],
            options={
                'verbose_name': '手机基本参数表',
                'verbose_name_plural': '手机基本参数表',
            },
        ),
        migrations.AddField(
            model_name='params',
            name='appearance',
            field=models.TextField(blank=True, verbose_name='外观'),
        ),
        migrations.AddField(
            model_name='params',
            name='camera',
            field=models.TextField(blank=True, verbose_name='摄像头'),
        ),
        migrations.AddField(
            model_name='params',
            name='function',
            field=models.TextField(blank=True, verbose_name='功能与服务'),
        ),
        migrations.AddField(
            model_name='params',
            name='hardware',
            field=models.TextField(blank=True, verbose_name='硬件'),
        ),
        migrations.AddField(
            model_name='params',
            name='net',
            field=models.TextField(blank=True, verbose_name='网络与连接'),
        ),
        migrations.AddField(
            model_name='params',
            name='pack',
            field=models.TextField(blank=True, verbose_name='手机附件'),
        ),
        migrations.AddField(
            model_name='params',
            name='protect',
            field=models.TextField(blank=True, verbose_name='保修信息'),
        ),
        migrations.AlterField(
            model_name='params',
            name='basic',
            field=models.TextField(blank=True, verbose_name='基本参数'),
        ),
        migrations.AlterField(
            model_name='params',
            name='screen',
            field=models.TextField(blank=True, verbose_name='屏幕'),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='params',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='info.Params', verbose_name='手机详细参数'),
        ),
        migrations.DeleteModel(
            name='Basic',
        ),
        migrations.DeleteModel(
            name='Screen',
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='basicparams',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='phone', to='info.BasicParams', verbose_name='手机基本参数'),
            preserve_default=False,
        ),
    ]