# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0004_auto_20150407_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classes',
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='checker.Student'),
        ),
    ]
