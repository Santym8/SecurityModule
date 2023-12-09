from django.contrib import admin
from .models import Role

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)

admin.site.register(Role, RoleAdmin)
