# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-10 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20170509_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=120),
        ),
    ]