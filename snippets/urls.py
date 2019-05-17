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
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import *

urlpatterns = [
    path('snippets/', SnippetListView.as_view()),
    path('snippets/<int:pk>', SnippetDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
