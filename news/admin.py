from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """Modyfikacja podstawowego zachowania widoku w panelu administracji."""

    class NewsInline(admin.StackedInline):
        model = models.News
        extra = 0

    @staticmethod
    def related_categories_number(obj):
        return obj.children.count()

    readonly_fields = ('id',)
    list_display = ('name', 'parent_category', 'related_categories_number')
    inlines = [NewsInline]


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    # class TagsInline(admin.StackedInline):
    #     model = models.Tag.through (?)
    #     extra = 1

    readonly_fields = ('id',)
    list_display = ('title', 'category')
    # inlines = [TagsInline]


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    @staticmethod
    def news_number(obj):
        return obj.news.count()

    list_display = ('name', 'news_number')

# admin.site.register(models.News, NewsAdmin)
