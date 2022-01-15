# Generated by Django 4.0 on 2022-01-15 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libmansys', '0012_rename_issued_requested_book_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='requested_book',
            name='reason',
            field=models.CharField(default='Provide a reason for rejection', max_length=50),
        ),
        migrations.AlterField(
            model_name='requested_book',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libmansys.book'),
        ),
        migrations.AlterField(
            model_name='requested_book',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libmansys.student'),
        ),
    ]