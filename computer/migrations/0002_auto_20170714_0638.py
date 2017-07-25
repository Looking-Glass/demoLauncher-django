# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='description',
        ),
        migrations.AddField(
            model_name='computer',
            name='existingApps',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='runningApp',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
