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

app_name = 'snippets'
urlpatterns = [
    path('', SnippetListView.as_view(), name='snippets-list'),
    path('<int:pk>/', SnippetDetailView.as_view(), name='snippets-detail'),

    path('users/', UserListView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='users-detail'),

    path('rootapi/', RootAPIView.as_view(), name='rootapi'),
    path('<int:pk>/highlight/', SnippetHighlight.as_view(), name='highlight'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
