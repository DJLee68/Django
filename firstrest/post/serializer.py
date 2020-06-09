from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer): #{
    class Meta:
        model = Post
        fields = '__all__' # or fields = ['title', 'body'] we can include 'id' also. 웬만하면 튜플로
        read_only_fields = ('title',)
        # you can add 'write only' option as well.
#}