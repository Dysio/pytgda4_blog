import hashlib
import os
import unicodedata
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe

from blog import settings


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

# pylint:disable=unused-argument
def user_photo_name(instance, filename):
    m = hashlib.md5()
    m.update(unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore'))
    file_extension = os.path.splitext(filename)
    return "{}{}".format(m.hexdigest(), file_extension[1])


class Profile(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True, default=None)
    photo = models.ImageField(blank=True, null=True, upload_to=user_photo_name)

    def image_tag(self):
        return mark_safe('<img src="%s/%s" width="100px" />' % (settings.MEDIA_URL, str(self.photo)))

    image_tag.short_description = 'Zdjęcie'
    image_tag.allow_tags = True

    def __str__(self):
        """Returns string representation as first_name last_name."""
        return '{} {} - {}'.format(self.last_name, self.first_name, self.username)
