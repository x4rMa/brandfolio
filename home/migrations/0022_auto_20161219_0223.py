# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 02:23
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20161218_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='headline',
            field=wagtail.wagtailcore.fields.StreamField((('title', wagtail.wagtailcore.blocks.TextBlock(blank=False, help_text='End Result Customer Wants + Specific Period Of Time + Address The Objections')), ('subtitle', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), ('cta', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock()), ('url', wagtail.wagtailcore.blocks.CharBlock()), ('target_blank', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Open link in a new tab?', required=False))), required=False)))),
        ),
    ]
