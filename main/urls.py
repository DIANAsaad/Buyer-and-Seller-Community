from django.urls import path
from main import views



urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.sign_up, name='sign_up'),
    path('logout',views.logout, name='logout')
            ]