# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0004_auto_20170330_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='title',
            field=models.CharField(default='Make title', max_length=255),
            preserve_default=False,
        ),
    ]