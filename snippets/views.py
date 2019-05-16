from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializer import SnippetSerializer


class SnippetListView(View):
    """
    列出所有的snippet
    """

    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        json_data = serializer.data
        return JsonResponse(json_data, safe=False)


class SnippetDetailView(View):
    """
    获取，更新或删除一个snippet
    """

    def get(self, request, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return JsonResponse(status=404, safe=False)

        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return JsonResponse(status=404, safe=False)

        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)

        else:
            return JsonResponse(serializer.errors, status=400, safe=False)

    def delete(self, request, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return JsonResponse(status=404, safe=False)

        snippet.delete()
        return JsonResponse(status=204, safe=False)
