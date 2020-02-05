from django.shortcuts import render
from .models import Makeblog

# Create your views here.

def home(request): #{
    blogs = Makeblog.objects
    return render(request, 'home.html', {'blogs' : blogs})
#}