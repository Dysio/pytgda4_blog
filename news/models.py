import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, null=False, blank=False)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                        related_name='children')

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


class Profile(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        """Returns string representation as first_name last_name."""
        return '{} {} - {}'.format(self.last_name, self.first_name, self.username)
