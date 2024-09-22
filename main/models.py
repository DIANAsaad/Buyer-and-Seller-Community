from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    price=models.FloatField()
    image_url=models.CharField(max_length=2083)


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
