# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160209_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='_summary_rendered',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='summary_markup_type',
            field=models.CharField(choices=[(b'', b'--'), (b'markdown', b'markdown')], default='markdown', editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=markupfield.fields.MarkupField(rendered_field=True),
        ),
    ]
