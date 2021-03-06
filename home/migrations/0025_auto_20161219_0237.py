# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 02:37
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20161219_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='cta',
            field=wagtail.wagtailcore.fields.StreamField((('title', wagtail.wagtailcore.blocks.TextBlock(blank=False, help_text='End Result Customer Wants + Specific Period Of Time + Address The Objections')), ('subtitle', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock()), ('url', wagtail.wagtailcore.blocks.CharBlock()), ('icon', wagtail.wagtailcore.blocks.CharBlock(blank=True, help_text='FontAwesome icon classname', max_length=50)), ('target_blank', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Open link in a new tab?', required=False))), required=False))))),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='headline',
            field=wagtail.wagtailcore.fields.StreamField((('title', wagtail.wagtailcore.blocks.TextBlock(blank=False, help_text='End Result Customer Wants + Specific Period Of Time + Address The Objections')), ('subtitle', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock()), ('url', wagtail.wagtailcore.blocks.CharBlock()), ('icon', wagtail.wagtailcore.blocks.CharBlock(blank=True, help_text='FontAwesome icon classname', max_length=50)), ('target_blank', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Open link in a new tab?', required=False))), required=False))))),
        ),
    ]
