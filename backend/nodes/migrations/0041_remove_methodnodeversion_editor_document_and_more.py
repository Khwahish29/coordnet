# Generated by Django 5.1.4 on 2025-01-13 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nodes", "0040_remove_methodnodeversion_document_version_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="methodnodeversion",
            name="editor_document",
        ),
        migrations.RemoveField(
            model_name="methodnodeversion",
            name="graph_document",
        ),
    ]
