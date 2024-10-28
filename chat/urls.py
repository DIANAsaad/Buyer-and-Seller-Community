from django.urls import path
from chat import views

urlpatterns=[
    path('chat',views.chat),
    path('message_creation', views.message_creation)
]