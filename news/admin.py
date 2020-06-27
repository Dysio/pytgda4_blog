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
    class TagsInline(admin.StackedInline):
        """
        Lista tagów wyświetlana od strony postów. Through jest o tyle istotne, że mówi admince django
        o istnieniu relacji wiele-wiele.

        Nie przejmujemy się także tym, że 'tags' jest oznaczone jako "unresolved attribute". Tags jest wirtualnym polem
        opisanym jako "related_name" w modelu Tag
        """
        model = models.News.tags.through
        extra = 1

    readonly_fields = ('id',)
    list_display = ('title', 'category')
    inlines = [TagsInline]


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    @staticmethod
    def news_number(obj):
        return obj.news.count()

    list_display = ('name', 'news_number')

admin.site.register(models.Profile)
