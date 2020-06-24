from django.shortcuts import render
from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets

# Create your views here.

class UserPostViewSet(viewsets.ModelViewSet): #{
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer 

    def get_queryset(self): #{
        # 여기 내부에서 쿼리셋을 관리하고 queryset 리턴하는게 효율적!
        qs = super().get_queryset()
        # qs = qs.filter(author__id = 2)

        # 지금 로그인한 유저의 글만 필터링 해라
        qs = qs.filter(author=self.request.user)
        
        # .filter .exclude
        return qs
    #}
#}
