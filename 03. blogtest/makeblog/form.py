from django import forms
from .models import Makeblog

class BlogPost(forms.ModelForm): #{
    class Meta: #{
        model = Makeblog
        fields = ['title', 'body']  
    #}
#}
