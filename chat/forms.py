from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Post, Comment, Like, Profile
from chat.models import ChatGroup, GroupMessage


class MessageForm(forms.ModelForm):
    class Meta:
        model=GroupMessage
        fields=['body']
        widget={
            'body':forms.TextInput(attrs={'placeholder':'Add Message...', 'class':'p-4 text-black', 'autofocus':True})
        }


