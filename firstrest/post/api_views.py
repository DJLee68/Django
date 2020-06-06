#데이터 처리 대상
from Posts.models import Post
from Posts.serializers import PostSerializer

# status에 따라 직접 Response를 처리할 것
from django.http import Http404 # Get Object or 404 직접 구현
from rest_framework.response import Response
from rest_framework import status

# APIView를 상속받은 CBV
from rest_framework.views import APIView
#Postdetail 클래스의 get_object 메소드 대신 이거 써도 된다
# from django.shortcuts import get_object_or_404

class PostList(APIView): #{
    def get(self, request, format=None): #{
        Posts = Post.object.all()
        serializer = PostSerializer(Posts, many=True)
        return Response(serializer.data)    
    #}

    def put(self, request, pk, format=None): #{
        
    #}
#}