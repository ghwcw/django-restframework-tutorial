#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------------------
    Creator : 汪春旺
       Date : 2019-05-16
    Project : rest_tutorial
   FileName : serializer.py
Description : 
-------------------------------------------------------------
"""
from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


# class SnippetSerializer(serializers.Serializer):
#     """
#     数据序列化
#     类似于Django表单
#     """
#
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         根据提供的验证过的数据创建并返回一个新的'Snippet'实例。
#         :param validated_data:需要创建的数据字典
#         :return: 'Snippet'实例
#         """
#
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
#         :param instance:实例
#         :param validated_data:更新的数据字典
#         :return:'Snippet'实例
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


# 使用Model序列化
class SnippetSerializer(serializers.ModelSerializer):
    """
    数据序列化    类似于Django表单。
    HyperlinkedModelSerializer：
        它包含一个url字段，使用HyperlinkedIdentityField；
        关联关系使用HyperlinkedRelatedField，而不是PrimaryKeyRelatedField。
    """""
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippets:highlight', read_only=True, format='html')

    class Meta:
        model = Snippet
        fields = '__all__'


# 用户信息序列化
class UserSerializer(serializers.ModelSerializer):
    # snippet = serializers.PrimaryKeyRelatedField(queryset=Snippet.objects.all(), many=True)

    class Meta:
        model = User

        fields = ['id', 'username',]



