from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewset_views
from rest_framework.urlpatterns import format_suffix_patterns
from . import api_views
from . import mixin_view
# django rest framework -> router를 이용해 url 결정

# router = DefaultRouter()
# router.register('post', views.PostViewset)
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
