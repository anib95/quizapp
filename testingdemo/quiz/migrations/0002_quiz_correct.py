# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='correct',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
