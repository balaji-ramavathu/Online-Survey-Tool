# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-12 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0026_auto_20180412_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='option3',
            field=models.CharField(default='anil', max_length=100),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option4',
            field=models.CharField(default='anil', max_length=100),
        ),
    ]
