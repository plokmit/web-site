# Generated by Django 4.2.1 on 2023-08-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_prefer_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='prefer_location',
            field=models.CharField(default='None', max_length=120),
        ),
    ]