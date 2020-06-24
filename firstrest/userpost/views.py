from django.shortcuts import render
from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets

# Create your views here.

class UserPostViewSet(viewsets.ModelViewSet): #{
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer 
#}
