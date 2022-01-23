# Generated by Django 4.0 on 2022-01-23 13:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmansys', '0020_alter_student_bits_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile_number',
            field=models.IntegerField(default=-1, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)]),
        ),
    ]