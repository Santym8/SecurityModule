from django.contrib import admin
from .models import Audit

class AuditAdmin(admin.ModelAdmin):
    list_display = ('id', 'action', 'description', 'observation', 'ip', 'user', 'function', 'date')
    list_filter = ('action', 'ip', 'user', 'function')
    search_fields = ('action', 'ip', 'user', 'function')

admin.site.register(Audit, AuditAdmin)
