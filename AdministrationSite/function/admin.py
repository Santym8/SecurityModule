from django.contrib import admin
from .models import Function

class FunctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)

admin.site.register(Function, FunctionAdmin)
