# Generated by Django 2.2 on 2019-07-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_cartitem_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='location',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]