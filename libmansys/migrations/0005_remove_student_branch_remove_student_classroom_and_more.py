# Generated by Django 4.0 on 2022-01-12 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("libmansys", "0004_alter_student_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="branch",
        ),
        migrations.RemoveField(
            model_name="student",
            name="classroom",
        ),
        migrations.RemoveField(
            model_name="student",
            name="image",
        ),
        migrations.RemoveField(
            model_name="student",
            name="phone",
        ),
        migrations.RemoveField(
            model_name="student",
            name="roll_no",
        ),
        migrations.RemoveField(
            model_name="student",
            name="user",
        ),
        migrations.AddField(
            model_name="student",
            name="username",
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
