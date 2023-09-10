from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_folder.models import Account

class Myadmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields =('id', 'date_joined', 'last_login')
    
    
    filter_horizontal =()
    fieldsets = ()
    list_filter = ()
    
    admin.site.register(Account)
