# Generated by Django 5.0.4 on 2024-05-06 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("permissions", "0003_remove_soft_deleted_permissions"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="objectmembership",
            name="is_removed",
        ),
    ]
