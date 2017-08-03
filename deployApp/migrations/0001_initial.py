# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('sex', models.TextField()),
                ('age', models.IntegerField()),
                ('birthDay', models.DateField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]