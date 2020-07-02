from django.shortcuts import render
from rest_framework import viewsets
from .models import Essay
from .serializers import EssaySerializer
from rest_framework.filters import  SearchFilter
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