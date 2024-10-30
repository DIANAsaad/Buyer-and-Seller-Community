from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
import json
from django.template.loader import render_to_string
from chat.models import ChatGroup,GroupMessage
#Here we have no access to the request object anymore, we can get info using the Scope dictionary

class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        self.user =self.scope["user"] #user
        self.chatroom_name=self.scope['url_route']['kwargs']['chatroom_name']
        self.chatroom=get_object_or_404(ChatGroup,group_name=self.chatroom_name)
        self.accept()
    def receive(self, text_data): #received data is in the format of json, we have to convert it to python object
        text_data_json=json.loads(text_data)
        body=text_data_json['body']
    #save message in db
        message=GroupMessage.objects.create(
           body= body,
           author= self.user,
           group=self.chatroom
        )
    #Send data to frontend
        context= {
        'message': message,
        'user':self.user,
         }
        html=render_to_string("chat_requierments/partials/chat_message_p.html", context=context)
        self.send(text_data=html)