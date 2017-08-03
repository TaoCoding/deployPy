# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.


class Users(models.Model):
    userId = models.CharField(max_length=50)
    sex = models.TextField(max_length=1)
    age = models.IntegerField(max_length=3)
    birthDay = models.DateField()
    address = models.CharField(max_length=100)

admin.site.register(Users, )

