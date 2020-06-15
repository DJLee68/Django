from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewset_views
from rest_framework.urlpatterns import format_suffix_patterns
from . import api_views
from . import mixin_view
# django rest framework -> router를 이용해 url 결정

# path(요청을 처리할 url, 요청을 인자로 받아 처리할 함수, namespace)
# 여러 함수를 묶어서 url로 처리 -> .as_view() 함수가 한다 -> 이걸 또 묶어주는게 router!

# router -> router.register(주소 prefix, view 함수)
router = DefaultRouter()
router.register('post', viewset_views.PostViewset)
    

# APIView 사용 시 Default Router 사용 x ==> API ROOT 없음.

urlpatterns = [
    # for viewset
    
    path('', include(router.urls)),
    
    # 127.0.0.1:8000/post == ListView
    # path('post/', mixin_view.PostList.as_view()),
    # # 127.0.0.1:8000/post/<pk> == DetailView
    # path('post/<int:pk>', mixin_view.PostDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
