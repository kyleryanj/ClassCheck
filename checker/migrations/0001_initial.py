# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_code', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[A-Fa-f]{4}\\d{6}', message=b'Invalid course code. Should be code+section e.g. csci110101')])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^\\+1\\d{10}$', message=b"Phone number must be entered in the format: '+19999999999'.")])),
                ('email', models.EmailField(max_length=70, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='checker.Student'),
        ),
    ]
