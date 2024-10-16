from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from main.models import Like, Comment, Notifications, Post

@receiver(post_save, sender=Comment)
def create_comment_notification(sender,instance,created,**kwargs):
    if created:
        comment_notification= Notifications.objects.create(
        user=instance.post.author,
        message=f"{instance.user.username} commented on your post!"
        )

@receiver(post_save, sender=Like)
def create_like_notification(sender,instance,created,**kwargs):
    liker=instance.user
    Like.objects.get_or_create(post=post,liker=liker)
    post=Post.objects.filter(author=post.user_id).first()
    if created:
        like_notification= Notifications.objects.create(
        user=instance.user,
        message=f"{instance.user.username} Liked your post!"
        )


