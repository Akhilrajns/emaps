# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0007_auto_20170716_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviews',
            field=models.TextField(blank=True, max_length=255, verbose_name='Reviews'),
        ),
    ]
