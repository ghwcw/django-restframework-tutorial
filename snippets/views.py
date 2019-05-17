from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializer import SnippetSerializer


class SnippetListView(APIView):
    """
    列出所有的snippet
    """

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetailView(APIView):
    """
    获取，更新或删除一个snippet
    """

    def get_object(self, pk):
        return get_object_or_404(Snippet, pk=pk)

    def get(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk=pk)
        serializer = SnippetSerializer(snippet, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return HttpResponse('id={0}，对象不存在'.format(pk), status=404)

        snippet.delete()
        return JsonResponse(status=204, safe=False)
