"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
import uuid

from rest_framework import serializers

from news.models import News, Category


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'category', 'category_name')

    def create(self, validated_data):
        """To tu działa POST!!! :P ."""
        news = News(**validated_data)
        news.save()
        return news

    def update(self, instance, validated_data):
        """A tu działa PUT i PATCH."""
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)

        # @todo - dlaczego POST nie działa w tym miejscu??? (patrz wyżej)
        category = validated_data.get('category', instance.category.id)

        try:
            category = uuid.UUID(category)
        except TypeError:
            category = Category.objects.get_or_create(name=category)[0]

        instance.category = category
        instance.category_name = validated_data.get('category_name', instance.category_name)

        instance.save()
        return instance
