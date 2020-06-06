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
        posts = Post.object.all()
        serializer = PostSerializer(posts, many=True) # 쿼리셋 넘기기 (다수의 객체를 seralize 시킬 땐, many=True인자)
        return Response(serializer.data) # 직접 Response 리턴해주기 : serializer.data    
    #}

    def post(self, request): #{
        serializer = Postderializer(data=request.data)
        if serializer.is_valid(): #{ 직접 유효성 검사
            serializer.save()     # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #}
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #}

    # Respone 인자 -> 1. 데이터 2. status 3. 템플릿
#}

# PostList 클래스와 달리 pk값을 받음 (메소드에 pk인자) 
class PostDetail(APIView): #{
    # get_object_or_404를 구현해주는 helper function
    def get_objet(self, pk): #{
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    #}

    def get(self, request, pk, format=None): #{
        post = self.get_objet(pk)
        # post = get_object_or_4-4(Post, pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    #}
    
#}