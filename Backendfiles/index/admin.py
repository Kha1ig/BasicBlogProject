from django.contrib import admin

# Register your models here.

from index.models import index_Post

@admin.register(index_Post)

class IndexAdmin(admin.ModelAdmin):
    list_display = ('image', 'post_name', 'post_type', 'post_date')
    list_display_links = list_display
    search_fields =('post_name', 'post_type')
    search_help_text = ('find by post name and post type')  
    empty_value_display = 'no data'
    list_filter =  ('post_date', 'post_name', 'post_type')

#admin.site.register(index_Post)