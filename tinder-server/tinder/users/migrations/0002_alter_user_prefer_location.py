# Generated by Django 4.2.1 on 2023-08-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prefer_location',
            field=models.CharField(max_length=120),
        ),
    ]