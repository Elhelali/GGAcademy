# Generated by Django 2.2 on 2019-07-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_profile_pickup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]