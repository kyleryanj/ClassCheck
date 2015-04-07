# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0003_auto_20150407_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(to='checker.Class'),
        ),
        migrations.AlterField(
            model_name='class',
            name='class_code',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[A-Fa-f]{4}\\d{6}$', message=b'Invalid course code. Should be code+section e.g. csci110101')]),
        ),
    ]
