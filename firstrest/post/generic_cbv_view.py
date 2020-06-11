from post.models import Post
from post.serializer import PostSerializer
from rest_framework import generics

# 다 mixin 상속받아서 한거다

class PostList(generics.ListCreateAPIView): #{ list와 create 함수를 묶어준다
    queryset = Post.objects.all()
    serializer_class = PostSerializer
#}

class PostDetail(generics.RetrieveUpdateDestroyAPIView): #{
    queryset = Post.objects.all()
    serializer_class = PostSerializer
#}
