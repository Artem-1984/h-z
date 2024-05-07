from django.contrib import admin
from .models import BlodPost,Blogers
# Register your models here.
@admin.register(BlodPost)
class BlodPostAdmin(admin.ModelAdmin):
    list_display = ('header','text')
@admin.register(Blogers)
class ComPostAdmin(admin.ModelAdmin):
    list_display = ('first_name','text')