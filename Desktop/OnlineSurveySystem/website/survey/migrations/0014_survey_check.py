# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_auto_20180404_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]
