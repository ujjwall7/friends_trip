# Generated by Django 3.2.12 on 2023-07-22 05:44

from django.db import migrations, models
import master.models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0009_alter_expense_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, default=2, upload_to=master.models.webp),
            preserve_default=False,
        ),
    ]