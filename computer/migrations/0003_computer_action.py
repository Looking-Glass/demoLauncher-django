# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0002_auto_20170714_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='action',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
