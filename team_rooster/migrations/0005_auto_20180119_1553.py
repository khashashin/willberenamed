# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_rooster', '0004_auto_20180117_1325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teams',
            options={'verbose_name_plural': 'Teams'},
        ),
        migrations.AddField(
            model_name='teams',
            name='use_other_template',
            field=models.BooleanField(default=True),
        ),
    ]
