from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SnippetList(APIView): #{
    def get(self, request, format=None): #{
        snippets = Snippet.object.all()
        serializer = SnippetSerializer(snippets, many=True)    
    #}
#}