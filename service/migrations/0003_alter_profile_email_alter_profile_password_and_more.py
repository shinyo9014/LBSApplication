# Generated by Django 4.1 on 2022-12-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "service",
            "0002_remove_profile_created_remove_profile_last_location_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile", name="email", field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="profile",
            name="password",
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name="profile",
            name="username",
            field=models.CharField(max_length=100),
        ),
    ]
