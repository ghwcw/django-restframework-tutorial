# from django.http import JsonResponse, HttpResponse
#
# # Create your views here.
# from django.shortcuts import get_object_or_404
# from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
# from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializer import SnippetSerializer

from rest_framework import generics


# 仅仅继承APIView
# class SnippetListView(APIView):
#     """
#     列出所有的snippet
#     """
#
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SnippetDetailView(APIView):
#     """
#     获取，更新或删除一个snippet
#     """
#
#     @staticmethod
#     def _get_object(pk):
#         return get_object_or_404(Snippet, pk=pk)
#
#     def get(self, request, pk):
#         snippet = self._get_object(pk=pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         snippet = self._get_object(pk=pk)
#         serializer = SnippetSerializer(snippet, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         snippet = self._get_object(pk=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# 继承混入类
# class SnippetListView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class SnippetDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk=pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk=pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk=pk)


# 继承更加简洁的通用视图类
class SnippetListView(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

