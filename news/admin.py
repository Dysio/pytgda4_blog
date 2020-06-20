from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """Modyfikacja podstawowego zachowania widoku w panelu administracji."""

    @staticmethod
    def related_categories_number(obj):
        return obj.children.count()

    readonly_fields = ('id',)
    list_display = ('name', 'parent_category', 'related_categories_number')


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title', 'category')



# admin.site.register(models.News, NewsAdmin)
