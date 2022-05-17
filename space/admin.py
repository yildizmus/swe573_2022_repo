from django.contrib import admin
from jmespath import search
from space.models.spacemodel import SpaceModel

@admin.register(SpaceModel)
class SpaceAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'created_date', 'member_list')
    search_fields=('title', 'content')
    list_filter=['created_date']

