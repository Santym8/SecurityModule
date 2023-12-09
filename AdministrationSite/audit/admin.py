from django.contrib import admin
from .models import Audit

class AuditAdmin(admin.ModelAdmin):
    list_display = ('id', 'action', 'description', 'observation', 'ip', 'user_name', 'function_id')
    list_filter = ('action', 'ip', 'user_name', 'function_id')
    search_fields = ('action', 'ip', 'user_name', 'function_id')

admin.site.register(Audit, AuditAdmin)
