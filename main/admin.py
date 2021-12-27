from django.contrib import admin

# Register your models here.
from main.models import *

class CharacterImageInline(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 3


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['category']
    search_fields = ['name', 'description']
    inlines = [CharacterImageInline]


admin.site.register(Category)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Genre)
