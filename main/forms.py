from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Post, Comment, Like, Profile



class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    first_name=forms.CharField(max_length=255)
    last_name=forms.CharField(max_length=255)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name']


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['description','image_url']


class CommentForm(forms.ModelForm):
     class Meta:
         model=Comment
         fields=['content']

class LikeForm(forms.ModelForm):
    class Meta:
        model=Like
        fields=[]

class ProfilForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profile_image_url']