# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-17 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20181117_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banners',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.User'),
        ),
    ]
