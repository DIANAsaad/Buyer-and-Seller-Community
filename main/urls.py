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
    path('delete_comment', views.delete_comment),
    path('create_profile', views.create_profile),
    path('profile/', views.profile),
    path('profile/<str:username>', views.profile, name='author-profile'),
    path('read_notifications',views.read_notifications)
            ] 