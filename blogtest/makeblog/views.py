from django.shortcuts import render
from .models import Makeblog

# Create your views here.

def home(request): #{
    blogs = Makeblog.objects
    shorten_body = blogs.summary()
    return render(request, 'home.html', {'blogs' : blogs, 'shorten_body':shorten_body})
#}