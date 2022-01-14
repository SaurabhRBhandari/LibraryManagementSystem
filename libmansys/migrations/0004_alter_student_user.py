# Generated by Django 4.0 on 2022-01-12 12:12

import django.contrib.auth.base_user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libmansys", "0003_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="user",
            field=models.CharField(
                max_length=200,
                verbose_name=django.contrib.auth.base_user.AbstractBaseUser.get_username,
            ),
        ),
    ]
