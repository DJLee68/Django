from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split(' ')

    return render(request, 'result.html', {'full':text, 'total' : len(words)})