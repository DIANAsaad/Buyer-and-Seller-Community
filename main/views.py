from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from main.forms import RegisterForm
from django.contrib.auth import get_user,login, logout, authenticate
# Create your views here.



def home(request):
   user = None
   if not request.user.is_anonymous:
      user=get_user(request)
   return render(request,'main/home.html',{'user':user})


def sign_up(request):
   if request.method=='POST':
      form=RegisterForm(request.POST)
      if form.is_valid():
         user=form.save()
         login(request, user)
         return redirect('/home')
   else:
      form=RegisterForm()
   return render(request,'registration/sign_up.html',{'form': form})

def logout(resquest):
   logout(resquest)
   return redirect('/login')
