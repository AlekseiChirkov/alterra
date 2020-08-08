from django.contrib import admin

from authentication.models import MyUser
from authentication.forms import UserChangeForm, UserCreationForm


class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'username', 'first_name', 'last_name', 'birthday', 'phone')
    list_display_links = ('email', 'username')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'birthday', 'phone')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'birthday', 'password1', 'password2'),
        })
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('id', )
    filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)

