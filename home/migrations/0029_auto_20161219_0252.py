# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 02:52
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20161219_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='cta',
            field=wagtail.wagtailcore.fields.StreamField((('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock()), ('url', wagtail.wagtailcore.blocks.CharBlock()), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Optional: FontAwesome icon classname', max_length=50, required=False)), ('target_blank', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Open link in a new tab?', required=False)))), icon='link')), ('docs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtaildocs.blocks.DocumentChooserBlock(), icon='doc-empty')))),
        ),
    ]