from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from main.forms import RegisterForm, PostForm
from django.contrib.auth import get_user,login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout
from main.models import Post

# Create your views here.



def welcome(request):
   return render (request,'main/welcome.html')

@login_required(login_url='/login')
def home(request):
   posts=Post.objects.all()
   for item in posts:
      return render(request,'main/home.html',{'posts':posts})


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

def user_logout(request):
   logout(request)
   return redirect('/')


@login_required(login_url='/login')
def create_post(request):
    if request.method=="POST":
       form=PostForm(request.POST)
       if form.is_valid():
          post=form.save(commit=False)
          post.author=request.user
          post=form.save()
          return redirect ('/home')
    else:
     form=PostForm()
    return render(request,'main/create_post.html',{'form':form})