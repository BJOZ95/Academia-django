from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Curso

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name','rol', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rol',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('rol',)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Curso)
