# Generated by Django 4.0 on 2022-01-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmansys', '0014_rename_bits_id_student_bits_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bits_id',
            field=models.CharField(default='NOT YET UPDATED', max_length=13),
        ),
    ]