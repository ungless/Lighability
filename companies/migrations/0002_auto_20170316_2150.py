# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-16 21:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]