# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Users

import json

# Create your views here.


def index(request):
    context = {}
    context['hello'] = 'hello world!'
    return render(request, 'index.html', context)


def hello(request):
    return HttpResponse(json.dumps({'username': 'test', 'age': 26}, sort_keys=True,
                      indent=4, separators=(',', ': ')))


