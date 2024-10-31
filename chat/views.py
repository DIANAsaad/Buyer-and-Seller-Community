from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from main.models import Post, Comment, Like, Profile, Notifications
from chat.models import GroupMessage,ChatGroup
from chat.forms import MessageForm
from django.shortcuts import HttpResponse



def chat(request):
    group=ChatGroup.objects.get(group_name="PublicChat")
    messages=GroupMessage.objects.filter(group=group).all()
    return render(request,'chat_requirements/chat.html', {'messages': messages})


def message_creation(request):
    if request.htmx:
        form=MessageForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.author=request.user
            message.group=ChatGroup.objects.get(group_name="PublicChat")
            message=form.save()
            context={'message':message,
                     'user':request.user}
            
                # Return only the new message HTML if it's an HTMX request
            return render(request, "chat_requirements/partials/chat_message_p.html",context)
               # Redirect normally if not HTMX
        else:
                # Redirect or return success if not HTMX
            return redirect('/chat')
    else:
          form=MessageForm() 
    
    return HttpResponse(status=404)

