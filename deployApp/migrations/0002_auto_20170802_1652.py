# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deployApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.TextField(max_length=1),
        ),
    ]
