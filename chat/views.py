from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from main.models import Post, Comment, Like, Profile, Notifications
from chat.models import GroupMessage,ChatGroup
from chat.forms import MessageForm
def chat(request):
    group=ChatGroup.objects.get(group_name="Public Chat")
    group_messages=GroupMessage.objects.filter(group=group).all()
    return render(request,'chat_requirements/chat.html', {'group_messages': group_messages})


def message_creation(request):
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.author=request.user
            message.group=ChatGroup.objects.get(group_name="Public Chat")
            message=form.save()
            if request.headers.get("HX-Request"):
                # Return only the new message HTML if it's an HTMX request
                return render(request, "chat_requirements/partials/chat_message_p.html", {"form": form, "message":message})
               # Redirect normally if not HTMX
    else:
          form=MessageForm() 
    
    return render(request,'chat_requirements/chat.html')

