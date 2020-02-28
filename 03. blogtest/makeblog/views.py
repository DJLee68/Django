from django.shortcuts import render, get_object_or_404, redirect
from .models import Makeblog
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def home(request): #{
    blogs = Makeblog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Make.objects.all()
    paginator = Paginator(blog_list, 3)
    return render(request, 'home.html', {'blogs' : blogs})
#}

def detail(request, blog_id): #{
    details = get_object_or_404(Makeblog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})
#}

def new(request): #{
    return render(request, 'new.html')
#}

def create(request): #{
    blog = Makeblog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_data = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
#}
