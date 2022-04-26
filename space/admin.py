from django.contrib import admin
from jmespath import search
from .models import Space

class SpaceAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'created_date')
    search_fields=('title', 'content')
    list_filter=['created_date']

admin.site.register(Space, SpaceAdmin)