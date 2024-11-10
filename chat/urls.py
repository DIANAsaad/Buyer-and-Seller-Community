from django.urls import path
from chat import views

urlpatterns=[
    path('chat',views.chat),
    path('message_creation', views.message_creation),
    path('chat/<int:user_id>', views.get_or_create_chatroom, name="private-chat"), #get/ create will get the chatroom then redirect it to the chat 
    path('chat/<str:chatroom_name>', views.chat, name="chatroom"),
]