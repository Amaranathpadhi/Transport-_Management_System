# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-07 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etms1', '0005_auto_20190507_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addbooking',
            name='emp_name',
        ),
        migrations.AddField(
            model_name='addbooking',
            name='emp_name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
