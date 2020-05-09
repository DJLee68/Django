from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog
# Create your views here.

class BlogView(ListView): #{ html 템플릿 : 블로그 리스트를 담은 html
    model = ClassBlog
#}
class BlogCreate(CreateView): #{ html: form(입력공간)을 가지고 있는 html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')
#}

class BlogDetail(DetailView): #{ html: 상세 페이지를 담은 html
    model = ClassBlog
#}
class BlogUpdate(UpdateView): #{ html: form(입력공간)을 가지고 있는 html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')
#}

class BlogDelete(DeleteView): #{ html: '이거 진짜 지울거야?'
    model = ClassBlog
    success_url = reverse_lazy('list')
#}

