from django.db import models
from django.conf import settings

# Create your models here.

class UserPost(models.Model): #{
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)
#}
# Default = 1 means 유저를 1번부터 시작한다!

# 1번 유저 - dj / 1234
# 2번 유저 - jm / 1234