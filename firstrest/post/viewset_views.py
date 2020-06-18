from django.shortcuts import render
from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets

# Custom API를 이용하기 위해(CRUD가 아닌 다른 함수 만드려고)
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework import renderers
from django.http import HttpResponse

# Pagination 클래스 따로 빼기(코드 리팩토링)
from .pagination import MyPagination


# Create your views here.

# CBV


# read-only 기능만 필요하면 Readonlymodelviewset 상속해서 클래스 만들면됨
# class PostReadViewSet(viewsets.ReadOnlyModelViewSet): #{
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
# #}

class PostViewset(viewsets.ModelViewSet): #{
    queryset = Post.objects.all().order_by('id') # 페이지네이션을 할 때는 반드시 레코드를 정렬한 상태에서 페이지네이션을 수행할 것!
    serializer_class = PostSerializer
    
    # Customized Pagination
    pagination_class = MyPagination

    # 권한 설정!
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # 이 액션을 실행할 수 있는 권한 설정(인증된 요청에서만)

    # 나만의 Custom API(로직)을 사용하고 싶을 때 / 내가 직접 view 구현하고 싶을 때
    # Custom API의 Default Method는 GET이다. 만약 Post 형식을 원하면 @action(method=['post'])로 설정
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) # renderers -> Response를 어떤 형식으로 Rendering 시킬 것인가
    
    #highlight라는 custom 함수 만들기
    def highlight(self, request, *args, **kwargs): #{
        return HttpResponse("얍")
    #}

    # def perform_create(self, serializer): #{
    #     serializer.save(owner=self.request.user)
    # #}
#}


