from django.shortcuts import render, get_object_or_404
from .models import Makeblog

# Create your views here.

def home(request): #{
    blogs = Makeblog.objects
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
    return
#}