from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('author', 'status', 'created', 'publish')
    orderiing = 'publish'
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
