from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# django rest framework -> router를 이용해 url 결정

router = DefaultRouter()
router.register('post', views.PostViewset)

urlpatterns = [
    path('', include(router.urls)),
]
