# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sclad', '0002_auto_20171010_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scladtov',
            name='kol',
            field=models.IntegerField(default=1),
        ),
    ]
