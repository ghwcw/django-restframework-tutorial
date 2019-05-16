#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------------------
    Creator : 汪春旺
       Date : 2019-05-16
    Project : rest_tutorial
   FileName : urls.py
Description : 
-------------------------------------------------------------
"""
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from snippets.views import *

urlpatterns = [
    path('snippets/', csrf_exempt(SnippetListView.as_view())),
    path('snippets/<int:pk>', csrf_exempt(SnippetDetailView.as_view())),
]

