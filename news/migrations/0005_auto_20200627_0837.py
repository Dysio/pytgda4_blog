# Generated by Django 3.0.7 on 2020-06-27 08:37

from django.db import migrations


def forwards_migrations(apps, schema_editor):
    # potrzebujemy modelu "Group" do dodawania grup użytkowników
    Group = apps.get_model("auth", "Group")

    # domyślny alias do bazy danych (o nazwie "defaulf")
    db_alias = schema_editor.connection.alias

    # tworzenie grup użytkownika
    Group.objects.using(db_alias).bulk_create([
        Group(name="Customer"),
        Group(name="Seller"),
        Group(name="Manager")
    ])


def rollback_migrations(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).filter(name__in=["Customer", "Seller", "Manager"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0004_tag'),
    ]

    operations = [
        migrations.RunPython(forwards_migrations, rollback_migrations)
    ]
