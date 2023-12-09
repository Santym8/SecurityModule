from django.contrib import admin
from .models import Module

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status')
    search_fields = ('name', 'description')

admin.site.register(Module, ModuleAdmin)
