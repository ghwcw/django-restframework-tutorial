# # Create your views here.
from django.http import JsonResponse, HttpResponse

from django.shortcuts import get_object_or_404
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import mixins, permissions
from rest_framework.decorators import detail_route

from rest_framework.parsers import JSONParser
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializer import SnippetSerializer, UserSerializer

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

# -----------------------------------------------------------------------

# class SnippetListView(generics.ListCreateAPIView):
#     """
#     继承更加简洁的通用视图类
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     # 添加视图权限
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     # 添加视图权限
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#
#
# class UserListView(generics.ListAPIView):
#     """
#     用户视图列表
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetailView(generics.RetrieveAPIView):
#     """
#     用户视图细节
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class RootAPIView(GenericAPIView):
#     """
#     为我们的API创建一个根视图
#     """
#
#     def get(self, request, format=None):
#         return Response({
#             'users': reverse('snippets:users-list', request=request, format=format),
#             'snippets': reverse('snippets:snippets-list', request=request, format=format)
#         })
#
#
# class SnippetHighlight(RetrieveAPIView):
#     """
#     为高亮显示的代码片段创建视图
#     """
#     queryset = Snippet.objects.all()
#     renderer_classes = [StaticHTMLRenderer]
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(data=snippet.highlight)


# -----------------------------------------------------------------------

# 使用ViewSets重构，继承涵盖ListModelView、RetrieveModelView、UpdateModelView等；
# 按Model分别写视图集合，一个Model一个视图集合。
class UserViewSet(ReadOnlyModelViewSet):
    """
    此视图自动提供`list`和`retrieve`操作。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(ModelViewSet):
    """
    此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(data=snippet.highlight)

