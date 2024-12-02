# Generated by Django 5.1.3 on 2024-11-26 15:48
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations


def move_relation_to_objects(apps, schema_editor):
    Profile = apps.get_model("profiles", "Profile")

    for profile in Profile.objects.all():
        if profile.new_user is not None:
            profile.new_user.profile = profile
            profile.new_user.save()
            continue
        if profile.new_space is not None:
            profile.new_space.profile = profile
            profile.new_space.save()


def move_relation_to_profile(apps, schema_editor):
    Profile = apps.get_model("profiles", "Profile")
    User = apps.get_model("users", "User")
    Space = apps.get_model("nodes", "Space")

    for profile in Profile.objects.all():
        try:
            profile.new_user = User.objects.get(profile_id=profile.id)
            profile.save()
            continue
        except ObjectDoesNotExist:
            pass
        try:
            profile.new_space = Space.objects.get(profile_id=profile.id)
            profile.save()
        except ObjectDoesNotExist:
            pass


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0004_remove_profile_is_public_profile_draft_and_more"),
        ("users", "0005_fill_profiles"),
        ("nodes", "0032_fill_profiles"),
    ]

    run_before = [
        ("users", "0007_remove_user_profile"),
        ("nodes", "0034_remove_space_profile"),
    ]

    operations = [migrations.RunPython(move_relation_to_profile, move_relation_to_objects)]
