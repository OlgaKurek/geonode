# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 21:20
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0032_auto_20180412_0822'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='document',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
