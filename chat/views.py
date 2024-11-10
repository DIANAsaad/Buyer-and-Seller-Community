from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from main.models import Post, Comment, Like, Profile, Notifications
from chat.models import GroupMessage,ChatGroup
from chat.forms import MessageForm
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, Group
from django.http import Http404

def chat(request, chatroom_name="PublicChat"):
    chat_group=ChatGroup.objects.get(group_name=chatroom_name)
    messages=GroupMessage.objects.filter(group=chat_group).all()  
    other_user=None   
    if chat_group.is_private:
          if request.user not in chat_group.members.all(): #Checking if loggen in user has permission to join
              raise Http404()
          for member in chat_group.members.all():
            if member != request.user:
                 other_user=member
                 break
            context={
           'messages':messages,
           'other_user':other_user,
           "chatroom_name":chatroom_name,
            }
            return render(request,'chat_requirements/chat.html', context)
    else:
        return render(request,'chat_requirements/chat.html', {'messages':messages})

     


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

@login_required
def get_or_create_chatroom (request,user_id):
    other_user=User.objects.get(id=user_id)
    my_chatrooms=ChatGroup.objects.filter(is_private=True,members=request.user) #I'm fetching all the cahtrooms of the logged in user

    if my_chatrooms.exists():
        for chatroom in my_chatrooms:
            if other_user in chatroom.members.all(): #checking to see if there ais a chatroom bewteen the user and the other user
                chatroom=chatroom
                break
            else:
                chatroom=ChatGroup.objects.create(is_private=True)
                chatroom.members.add(other_user, request.user)
    else:
         chatroom=ChatGroup.objects.create(is_private=True,group_name=f'chat with {other_user.username}')
         chatroom.members.add(other_user, request.user)
       

    return redirect('chatroom', chatroom.group_name)