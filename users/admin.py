from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.models import Group
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'email',  'is_staff')
    
    
admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)    