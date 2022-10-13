from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'first_name','middle_name','last_name')
    list_filter = ('email', 'first_name', 'last_name', 'is_active')
    ordering = ('-joined_date',)
    list_display = (
        'email',
        'first_name',
        'middle_name',
        'last_name',
        'is_active',
        'is_staff'
    ) 

    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'middle_name', 'last_name')}),
        ('Permissions', {"fields": ("is_staff", "is_active")}),
        ('Groups', {"fields": ("groups",)}),
        ("User permissions", {"fields": ('user_permissions', )})
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide', ),
                'fields': (
                    'email',
                    'first_name',
                    'middle_name',
                    'last_name',
                    'password',
                    'is_active',
                    'is_staff',
                ),
            },
        ),
    )




admin.site.register(NewUser, UserAdminConfig)