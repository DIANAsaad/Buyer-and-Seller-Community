from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from main.forms import RegisterForm, PostForm
from django.contrib.auth import get_user,login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout as logout
from main.models import Post
from django.contrib.auth.models import User, Group

# Create your views here.


def welcome(request):
   if request.user.is_authenticated:
      return redirect("/home")
   return render (request,'main/welcome.html')

@login_required(login_url='/login')
def home(request):
   posts=Post.objects.all()
   if request.method=="POST":
      post_id=request.POST.get("post-id")
      if post_id:
         post=Post.objects.filter(id=post_id).first()
         if post and (post.author==request.user or request.user.has_perm("main.delete_post")):
            post.delete()    
   for item in posts:
      return render(request,'main/home.html',{'posts':posts})
   

@login_required(login_url='/login')
def ban(request):
   if request.method=="POST":
      user_id=request.POST.get("user-id")
      if user_id:
         user=User.objects.filter(id=user_id).first()
         if user:
              group=Group.objects.filter(name='default')
              group.user_set.remove(user) 
      return redirect ('/home')





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

@permission_required("main.add_post",login_url="/login", raise_exception=True)
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

