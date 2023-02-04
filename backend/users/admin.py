from django.contrib import admin

from rest_framework.authtoken.models import Token

from users.models import Follow, User


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['key', 'user']
    search_fields = ['key', 'user__username']
    ordering = ['-created']
    verbose_name = 'Токен'
    verbose_name_plural = 'Токены'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions',
            {'fields': ('is_active', 'is_staff',
                        'is_superuser', 'groups', 'user_permissions')}),
    )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user', 'author')
    list_filter = ('user', 'author')
