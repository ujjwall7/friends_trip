# Generated by Django 3.2.12 on 2023-07-21 04:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20230721_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user', models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
