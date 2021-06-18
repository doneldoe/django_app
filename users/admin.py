from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = Profile
    search_fields = ('email', 'last_name', 'first_name', 'patronymic')
    list_filter = ('email', 'last_name', 'first_name', 'patronymic', 'is_active', 'is_staff')
    ordering = ('email',)
    list_display = ('email', 'last_name', 'first_name', 'patronymic', 'phone_number', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': (
            'email', 'last_name', 'first_name', 'patronymic', 'phone_number', 'passport_image', 'cam_image',
            'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Profile, UserAdminConfig)
