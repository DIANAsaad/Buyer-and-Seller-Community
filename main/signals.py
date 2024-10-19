from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.contrib.auth.models import User
from main.models import Like, Comment, Notifications, Post


@receiver(post_save, sender=Comment)
def create_comment_notification(sender,instance,created,**kwargs):
    author=instance.author
    post=instance.post
    post_owner=post.author
    if created:
        comment_notification= Notifications.objects.create(
        message=f"{instance.author} commented on your post!",
        engager_id=author.id,
        receiver=post_owner,
        )
        comment_notification.save()


@receiver(post_save, sender=Like)
def create_like_notification(sender,instance,created,**kwargs):
    liker=instance.liker
    post=instance.post
    post_owner=post.author
    if created:
        like_notification= Notifications.objects.create(
        message=f"{instance.liker} liked your post!",
        engager_id=liker.id,
        receiver=post_owner,
        )
        like_notification.save()


