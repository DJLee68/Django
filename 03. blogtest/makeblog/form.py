from django import forms
from .models import Makeblog

class BlogPost(forms.Form): #{
    email = form.EmailField()
    files = forms.FileField()
#}
