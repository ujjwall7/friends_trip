# Generated by Django 3.2.12 on 2023-08-11 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_alter_faqcategory_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqcategory',
            name='slug',
        ),
    ]
