from django.contrib import admin

# Register your models here.

from contact.models import Contact

@admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_display_links = list_display
    search_fields =('name', 'email')
    search_help_text = ('find by name and email')  
    empty_value_display = 'no data'
    list_filter =  ('name', 'email', )

#admin.site.register(Contact)
