from django.urls import path
from .consumers import * # .consumers is like the views.py (for logic)

websocket_urlspatterns = [
    path("ws/chatroom/<chatroom_name>",ChatroomConsumer.as_asgi()), #ws stands for websocket/chatroom/room_name (any parameter)
]