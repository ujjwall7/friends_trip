# Generated by Django 3.2.12 on 2023-07-22 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0008_auto_20230722_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
