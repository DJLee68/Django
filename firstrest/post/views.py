from django.shortcuts import render
from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets

# Create your views here.

# CBV

class PostViewset(viewsets.ModelViewSet): #{
    queryset = Post.objects.all()
    serializer_class = PostSerializer
#}
