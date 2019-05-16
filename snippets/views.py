from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from snippets.models import Snippet
from snippets.serializer import SnippetSerializer


class SnippetListView(View):
    def get(self):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        json_data = serializer.data
        return JsonResponse(json_data)



