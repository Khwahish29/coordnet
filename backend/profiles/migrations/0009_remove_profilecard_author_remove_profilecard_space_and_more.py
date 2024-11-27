# Generated by Django 5.1.3 on 2024-11-27 13:11

import django.db.models.deletion
import profiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0008_remove_profilecard_profile_profile_cards"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profilecard",
            name="author",
        ),
        migrations.RemoveField(
            model_name="profilecard",
            name="space",
        ),
        migrations.AddField(
            model_name="profilecard",
            name="author_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="author_cards",
                to="profiles.profile",
                validators=[profiles.models.validate_user_profile_public],
            ),
        ),
        migrations.AddField(
            model_name="profilecard",
            name="space_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="profiles.profile",
                validators=[profiles.models.validate_space_profile_public],
            ),
        ),
    ]
