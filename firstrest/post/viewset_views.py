from django.shortcuts import render
from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

# CBV


# read-only 기능만 필요하면 Readonlymodelviewset 상속해서 클래스 만들면됨
class PostViewset(viewsets.ModelViewSet): #{
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # 권한 설정!
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # 이 액션을 실행할 수 있는 권한 설정(인증된 요청에서만)

    # 나만의 Custom API(로직)을 사용하고 싶을 때 / 내가 직접 view 구현하고 싶을 때
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs): #{
        snippet = self.get_object()
        return Response(snippet.highlighted)
    #}

    def perform_create(self, serializer): #{
        serializer.save(owner=self.request.user)
    #}
#}
