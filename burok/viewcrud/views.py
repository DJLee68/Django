from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone 
from .models import Blog
from .forms import NewBlog

# Create your views here.

def welcome(request): #{
    return render(request, 'viewcrud/index.html')
#}

def read(request): #{
    blogs = Blog.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'blogs':blogs})
#}

def create(request)



