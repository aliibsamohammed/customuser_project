from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import AdminSite
from .models import CustomUser


class CustomUserAdmin(AdminSite):
    site_header = 'CustomUser Administration'
    site_title = 'CustomUser Site Admin'
    index_title = 'CustomUser Site Admin Home'


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, 
            {'fields': ('email', 'password', )}),
        (_('Personal info'), 
            {'fields': ('first_name', 'last_name', 'dob')}),
        (_('Permissions'), 
            {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (_('Important dates'),
            {'fields': ('last_login', 'date_mod')}),
        (_('user_info'), 
            {'fields': ('gender', 'mobile_phone')}),
    )

    add_fieldsets = (
       (None, {
           'classes': ('wide', ),
           'fields': ('email', 'password1', 'password2'),
       }),
    )

    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'dob', 'role', 'mobile_phone']
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', )

admin.site.register(CustomUser, CustomUserAdmin)
"""
admin.site.register(CustomUser)
"""
