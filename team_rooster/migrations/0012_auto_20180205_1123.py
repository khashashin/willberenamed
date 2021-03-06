# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-05 10:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtailblocks_cards.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('team_rooster', '0011_auto_20180205_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamrooster',
            name='spieler',
            field=wagtail.wagtailcore.fields.StreamField((('spieler', wagtailblocks_cards.blocks.CardsBlock(wagtail.wagtailcore.blocks.StructBlock((('photo', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('nummer', wagtail.wagtailcore.blocks.IntegerBlock(required=True)), ('name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('vorname', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('th', 'TH'), ('st', 'ST'), ('vt', 'VT')], icon='cup')), ('jahrgang', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[], help_text='Use the following format: <YYYY>', validators=[django.core.validators.MinValueValidator(1999), django.core.validators.MaxValueValidator(2018)])))), icon='user')),), blank=True),
        ),
    ]
