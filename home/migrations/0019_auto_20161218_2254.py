# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 22:54
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20161217_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='headline_sub',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='headline',
            field=wagtail.wagtailcore.fields.StreamField((('cta', wagtail.wagtailcore.blocks.StructBlock((('target_blank', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Open link in a new tab?', required=False)),), required=False)),)),
        ),
    ]