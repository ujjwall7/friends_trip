# Generated by Django 4.2.1 on 2023-06-15 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='mobile',
        ),
    ]
