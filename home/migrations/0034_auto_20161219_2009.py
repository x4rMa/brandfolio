# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 20:09
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20161219_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='cta',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock()), ('subtitle', wagtail.wagtailcore.blocks.RichTextBlock(required=False))), icon='title')), ('actions', wagtail.wagtailcore.blocks.StreamBlock((('link', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock()), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Optional: FontAwesome icon classname', max_length=50, required=False)), ('target_blank', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Open link in a new tab?', required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock())), icon='link')), ('doc', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock()), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Optional: FontAwesome icon classname', max_length=50, required=False)), ('target_blank', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Open link in a new tab?', required=False)), ('doc', wagtail.wagtaildocs.blocks.DocumentChooserBlock())), icon='doc-empty'))), icon='pick')))),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='social_proof',
            field=wagtail.wagtailcore.fields.RichTextField(help_text='E.g. 37signals is famous for this. Basecamphq.com - “millions of people use basecamp”'),
        ),
    ]
