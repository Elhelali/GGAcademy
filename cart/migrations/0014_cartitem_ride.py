# Generated by Django 2.2 on 2019-07-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_cartitem_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='ride',
            field=models.BooleanField(default=False),
        ),
    ]
