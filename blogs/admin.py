from django.contrib import admin

from blogs.models import Post, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'body', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'author', 'publish', 'status', 'slug')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('header', 'body')
    prepopulated_fields = {'slug': ('header',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
