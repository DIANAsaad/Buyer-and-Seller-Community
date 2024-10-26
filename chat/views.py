from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from main.models import Post, Comment, Like, Profile, Notifications
from chat.models import GroupMessage,ChatGroup

def chat(request):
    group=ChatGroup.objects.get(group_name="Public Chat")
    group_messages=GroupMessage.objects.filter(group=group).all()
    return render(request,'chat_requirements/chat.html', {'group_messages': group_messages})
