# Generated by Django 3.2.12 on 2023-07-22 03:10

from django.db import migrations, models
import master.models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_personalexpense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='image',
            field=models.ImageField(blank=True, upload_to=master.models.webp),
        ),
    ]