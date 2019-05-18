#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------------------
    Creator : 汪春旺
       Date : 2019-05-18
    Project : resttutorial
   FileName : permissions.py
Description : 
-------------------------------------------------------------
"""
from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        只允许对象的所有者编辑它
        """
        # 读权限
        if request.method in permissions.SAFE_METHODS:
            return True
        # 只有该snippet的所有者才允许写权限
        return obj.owner == request.user

