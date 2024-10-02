from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from main.forms import RegisterForm, PostForm, CommentForm
from django.contrib.auth import get_user,login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout as logout
from main.models import Post, Comment, Like
from django.contrib.auth.models import User, Group
from django.contrib import messages
# Create your views here.


def welcome(request):
   if request.user.is_authenticated:
      return redirect("/home")
   return render (request,'main/welcome.html')

@login_required(login_url='/login')
def home(request):
   posts=Post.objects.prefetch_related('comment_set').all()
   if request.method=="POST":
      post_id=request.POST.get("post-id")
      if post_id:
         post=Post.objects.filter(id=post_id).first()
         if post and (post.author==request.user or request.user.has_perm("main.delete_post")):
            post.delete()    
 
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


#User&Post operations


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

@login_required(login_url='/login')
def add_comment(request):
  if request.method=="POST":
       form=CommentForm(request.POST)
       if form.is_valid():
         comment=form.save(commit=False)
         post_id=request.POST.get('post-id')
         comment.post=Post.objects.get(id=post_id)
         comment.author=request.user
         comment.save()    
       else:
          form=CommentForm() 
  return redirect('/home')

@login_required(login_url='/login')
def ban(request):
   if request.method=="POST" and request.user.is_staff:
      user_id=request.POST.get("user-id")
      if user_id:
         user=User.objects.filter(id=user_id).first()
         if user:
              group=Group.objects.filter(name='default').first()
              group.user_set.remove(user) 
      return redirect ('/home')

@login_required(login_url='/login')
def like(request):
    if request.method=='POST':
           post_id=request.POST.get('post-id')
           post=Post.objects.filter(id=post_id).first()
           liker=request.user
           like, created= Like.objects.get_or_create(liker,post)
           if not created: 
              like.delete()
    return redirect('/home')
