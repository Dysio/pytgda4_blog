import uuid

from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, null=False, blank=False)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=150, null=False, blank=False)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'


class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)
    news = models.ManyToManyField(News, related_name='tags')

    def __str__(self):
        return self.name

class Login(models.Model):
    nick = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return self.nick

