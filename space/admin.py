from django.contrib import admin
from jmespath import search
from space.models import SpaceModel, MessageModel

@admin.register(SpaceModel)
class SpaceAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'created_date', 'member_list')
    search_fields=('title', 'content')
    list_filter=['created_date']

@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    list_display=('sender', 'memberspace', 'message', 'created_time')
    search_fields=('sender__username',)    