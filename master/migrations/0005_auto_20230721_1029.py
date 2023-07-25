# Generated by Django 3.2.12 on 2023-07-21 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import master.models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identity',
            field=models.UUIDField(null=True),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('price_distibuted', models.IntegerField()),
                ('image', models.ImageField(upload_to=master.models.webp)),
                ('description', models.TextField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip', to='master.trip')),
                ('user', models.ManyToManyField(related_name='expense_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
