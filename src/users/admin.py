from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext as __

from .models import User

admin.site.empty_value_display = __('(None)')
admin.site.site_header = 'mosh_social2'

admin.site.unregister(Group)


@admin.register(User)
class MyUser(UserAdmin):
    fieldsets = (
        (None, {
            'classes': ('extrapretty',),
            'fields': ('username', 'profile_pic', 'date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser',)
        }),
        ('Additional Information', {
            'classes': ('extrapretty', 'collapse',),
            'fields': ('password', 'email', 'first_name', 'last_name',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('extrapretty',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'profile_pic',)
        }),
    )
    list_display = ('id', 'username', 'date_joined', 'last_login',)
    list_display_links = ('id', 'username', 'date_joined', 'last_login',)
    list_filter = ('is_superuser',)
    search_fields = ('^username',)
    ordering = ('-id',)
    show_full_result_count = False
