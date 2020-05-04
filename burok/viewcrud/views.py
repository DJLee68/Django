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

def create(request): #{
    # 새로운 데이터 새로운 블로그 글을 저장하는 역할 == POST
    # 글쓰기 페이지를 띄워주는 역할 == GET

    if request.method == 'POST': #{
        # 입력된 블로그 글들을 저장해라
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_data = timezone.now()
            post.save()
            return redirect('home')
    #}

    else: #{
        # 단순히 입력받을 수 있는 form을 띄워줘라
        form = NewBlog()
        return render(request, 'viewcrud/new.html', {'form' : form})
    #}

    return 
#}

def update(request, pk): #{
    # 어떤 블로그를 수정할 지 블록 객체를 갖고기
    blog = get_object_or_404(Blog, pk = pk)

    # 해당하는 블로그 객체의 입력공간
    
    return
#}

def delete(request, pk): #{
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')
#}
