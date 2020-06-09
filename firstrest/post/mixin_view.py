# 데이터 처리 대상 : 모델, Serializer import 시키기
from post.models import Post
from post.serializer import PostSerializer

from rest_framework import mixins
from rest_framework import generics

class PostList(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView): #{
    queryset = Post.objects.all() # 쿼리셋 등록!
    serializer_class = PostSerializer # Serializer 클래스 등록!

    # get은 list 메소드를 나타내는 메소드
    def get(self, request, *args, **kwargs): #{
        return self.list(request, *args, **kwargs)
    #}

    # post는 create을 내보내는 메소드
    def post(self, request, *args, **kwargs): #{
        return self.create(request, *args, **kwargs)
    #}
#}