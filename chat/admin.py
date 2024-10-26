from django.contrib import admin
from chat.models import ChatGroup, GroupMessage
# Register your models here.


class ChatGroupAdmin(admin.ModelAdmin):
    list_display=('group_name',) 
    
class GroupMessageAdmin(admin.ModelAdmin):
    list_display=('group','author','body')
    
admin.site.register(ChatGroup, ChatGroupAdmin)
admin.site.register(GroupMessage,GroupMessageAdmin)