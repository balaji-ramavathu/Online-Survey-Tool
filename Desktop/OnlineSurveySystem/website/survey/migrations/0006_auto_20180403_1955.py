# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20180403_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.user'),
        ),
    ]
