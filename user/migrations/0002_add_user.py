from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations


def add_user(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
    User.objects.create(
        email="migrated@user.com",
        password=make_password("userpassword"),
        first_name="Migrated",
        last_name="Improved User",
    )


def remove_user(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
    User.objects.get(email="migrated@user.com").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(add_user, remove_user),
    ]
