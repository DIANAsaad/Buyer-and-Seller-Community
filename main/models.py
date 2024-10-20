from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    image_url=models.CharField(max_length=2083)


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()


class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    liker=models.ForeignKey(User,on_delete=models.CASCADE)
    liked_on = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('post', 'liker') 


class Profile(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_image_url=models.CharField(max_length=2083)
    bio=models.CharField(max_length=2083)

class Notifications(models.Model):
    engager=models.ForeignKey(User,related_name='engaged_notifications', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver_notifications', on_delete=models.CASCADE, default=None)
    message=models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
