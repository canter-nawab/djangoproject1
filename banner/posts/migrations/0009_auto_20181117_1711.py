# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-17 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20181117_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banners',
            name='name',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
