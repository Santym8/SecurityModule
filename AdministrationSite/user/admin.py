from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','dni','password','status')
    search_fields = ('username','email','dni','password','status')
    list_filter = ('username','email','dni','password','status')
    ordering = ('username','email','dni','password','status')


admin.site.register(User, UserAdmin)