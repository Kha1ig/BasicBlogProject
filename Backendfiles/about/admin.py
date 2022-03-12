from django.contrib import admin

# Register your models here.

from about.models import about_Post,about_work

admin.site.register(about_Post)
admin.site.register(about_work)