"""rest_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets.views import *

# 创建视图集合路由器并注册我们的视图。
# router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', SnippetListView.as_view(), name='home'),
    # path('snippets/', include('snippets.urls')),      # snippets App
    # path('users/', UserListView.as_view(), name='users-list'),
    # path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('login-out/', include('rest_framework.urls')),     # 登录和退出

    # router路由器配置
    # path('', include(router.urls)),

    # 配置视图集合路由：as_view({'action方法': '对象操作方法'})
    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'})),

    path('', SnippetViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('snippets/', SnippetViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('snippets/<int:pk>/', SnippetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('snippets/<int:pk>/highlight/', SnippetViewSet.as_view({'get': 'get_highlight'}, renderer_classes=[StaticHTMLRenderer])),

]


