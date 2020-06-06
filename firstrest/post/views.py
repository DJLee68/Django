from django.shortcuts import render
from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets
from rest_framework.urlpatterns import format_suffix_patterns
# Create your views here.

# CBV

class PostViewset(viewsets.ModelViewSet): #{
    queryset = Post.objects.all()
    serializer_class = PostSerializer
#}
