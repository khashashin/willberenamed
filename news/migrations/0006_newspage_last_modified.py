# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-05 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_newspage_date_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspage',
            name='last_modified',
            field=models.DateField(auto_now=True, verbose_name='Date article published'),
        ),
    ]
