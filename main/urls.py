from django.urls import path
from main import views



urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.welcome, name='welcome'),
    path('logout',views.logout, name='logout'),
    path('sign-up',views.sign_up),
            ]