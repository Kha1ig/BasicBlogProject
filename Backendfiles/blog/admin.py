from django.contrib import admin

# Register your models here.

from blog.models import blog_header, blog_Post, Comment

admin.site.register(blog_header)
admin.site.register(blog_Post)
admin.site.register(Comment)