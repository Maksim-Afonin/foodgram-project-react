from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy
from rest_framework.authtoken.models import Token

from users.models import Follow, User


admin.site.unregister(Group)
admin.site.unregister(TokenProxy)


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['key', 'user']
    search_fields = ['key', 'user__username']
    ordering = ['-created']
    verbose_name = 'Токен'
    verbose_name_plural = 'Токены'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Для модели пользователей включена фильтрация по имени и email
    """
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user', 'author')
    list_filter = ('user', 'author')
