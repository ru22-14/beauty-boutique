# Generated by Django 3.2.21 on 2023-10-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='confirmation_number',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
