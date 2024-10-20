from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from main.models import Post, Comment, Like, Profile, Notifications

def chat(request):
    return render(request,'chat_requirements/chat.html')
