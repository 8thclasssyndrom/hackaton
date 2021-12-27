from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Category)
admin.site.register(Character)
admin.site.register(Genre)
