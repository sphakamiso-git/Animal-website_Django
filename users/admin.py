from django.contrib import admin
from .models import CustomUser, SubscribedUsers

# Register your models here.

class SubscribedUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')
admin.site.register(CustomUser)
admin.site.register(SubscribedUsers, SubscribedUserAdmin)