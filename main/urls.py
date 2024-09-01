from django.urls import path
from main import views



urlpatterns=[
    path('',views.home),
    path('home',views.home,name='home'),
    path('sign-up',views.sign_up, name='sign_up'),
            ]