from django.contrib import admin

from .models import (
    Recipe, Tag, Ingredient, IngredientAmount, ShoppingCart, Favorite)


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Через админку можно добавить рецепт без ингредиентов.
    Так как связь идет через ManyToMany.
    """
    list_display = ('id', 'name', 'author', 'amount_favorites',
                    'amount_tags', 'amount_ingredients')
    list_filter = ('author', 'name', 'tags')
    search_fields = ('name',)
    inlines = [IngredientAmountInline]

    @staticmethod
    def amount_favorites(obj):
        return obj.favorites.count()

    @staticmethod
    def amount_tags(obj):
        return "\n".join([i[0] for i in obj.tags.values_list('name')])

    @staticmethod
    def amount_ingredients(obj):
        return "\n".join([i[0] for i in obj.ingredients.values_list('name')])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(IngredientAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'amount')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
