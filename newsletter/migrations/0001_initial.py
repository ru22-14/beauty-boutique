# Generated by Django 3.2.21 on 2023-10-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('confirmation_number', models.CharField(max_length=20)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
