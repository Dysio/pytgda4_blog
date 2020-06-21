# Generated by Django 3.0.7 on 2020-06-20 09:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200620_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='news.Category'),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='news.Category')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]