from django.shortcuts import render
from rest_framework import viewsets
from .models import Essay, Album, Files
from .serializers import EssaySerializer, AlbumSerializer, FilesSerializer
from rest_framework.filters import  SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


class PostViewSet(viewsets.ModelViewSet): #{
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer
   
    # 검색 기능!
    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')

    def perform_create(self, serializer): #{
        serializer.save(author=self.request.user)
    #}

    # 현재 request를 보낸 유저 == self.request.user

    def get_queryset(self): #{
        # 쿼리셋 먼저 가져와서
        qs = super().get_queryset()
        if self.request.user.is_superuser: #{
            qs = qs.all()
        #}
        else: #{
            if self.request.user.is_authenticated: #{
                qs = qs.filter(author = self.request.user)
            #}
            else:
                qs = qs.none()
        #}

        return qs
    #}
#}


class ImageViewSet(viewsets.ModelViewSet):#{
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer 
  
    def perform_create(self, serializer): #{
        serializer.save(author=self.request.user)
    #}
#}

class FileViewSet(viewsets.ModelViewSet): #{
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
    def perform_create(self, serializer): #{
        serializer.save(author=self.request.user)
    #}
    from rest_framework.response import Response
    from rest_framework import status

    # parser_class 지정(다양한 파일의 형식을 받아주는 방법들)
    parser_class = (MultiPartParser, FormParser)

    # create() -> POST 요청 오버라이딩

    def post(self, request, *args, **kwargs): #{
        serializer = FilesSerializer(data = request.data)
        if serializer.is_valid(): #{
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)
        #}
    #}
#}