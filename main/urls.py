from django.urls import path
from main import views



urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.welcome, name='welcome'),
    path('user_logout',views.user_logout, name='user_logout'),
    path('sign-up',views.sign_up),
    path('create_post',views.create_post),
    path('ban',views.ban),
    path('add_comment',views.add_comment),
    path('like',views.like, name='like'),
            ]