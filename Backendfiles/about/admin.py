from django.contrib import admin

# Register your models here.

from about.models import (
                about_Post,
                about_work,
                )

@admin.register(about_Post)

class about_postAdmin(admin.ModelAdmin):
    list_display = ('about_name','about_title', 'image', 'about_who',)
    list_display_links = list_display
    empty_value_display = 'no data'


@admin.register(about_work)

class about_workAdmin(admin.ModelAdmin):
    list_display = ('work_name',)
    list_display_links = ('work_name',)
    empty_value_display = 'no data'


#admin.site.register(about_Post)
#admin.site.register(about_work)