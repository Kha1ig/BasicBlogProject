from re import search
from django.contrib import admin
from blog.models import blog_Post
# Register your models here.

from blog.models import blog_header, blog_Post, Comment, commenter

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'author_position', 'blog_date', 'author_image')
    prepopulated_fields = {'author': ('author',)}
    prepopulated_fields = {'title': ('title',)}


admin.site.register(blog_header)
admin.site.register(blog_Post, PostAdmin)
@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog', 'letter', 'date_add',)
    list_filter = ('status', 'date_add', )
    search_fields = ('name', 'email', 'letter',)
    actions = ['approve_comments']
    

    def approve_comments(self, request, queryset):
        queryset.update(status = 'approve')

@admin.register(commenter)
class CommenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog',)
    search_fields = ('name', 'blog',)


