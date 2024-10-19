from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.contrib.auth.models import User
from main.models import Like, Comment, Notifications, Post


@receiver(post_save, sender=Comment)
def create_comment_notification(sender,instance,created,**kwargs):
    author=instance.author
    post=instance.post
    post_owner=post.author
    user=User.objects.filter(id=post_owner.id).first()
    if created:
        comment_notification= Notifications.objects.create(
        message=f"{instance.author} commented on your post!",
        engager_id=author.id,
        receiver_id=user.id,
        )
        comment_notification.save()


@receiver(post_save, sender=Like)
def create_like_notification(sender,instance,created,**kwargs):
    liker=instance.liker
    post=instance.post
    post_owner = post.author
    user=User.objects.filter(id=post_owner.id).first()
    if created:
        like_notification= Notifications.objects.create(
        message=f"{instance.liker} Liked your post!",
        engager_id=liker.id,
        receiver_id=user.id
        )
        like_notification.save()


