# Generated by Django 2.2 on 2019-07-13 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_orderitem_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='location',
            field=models.CharField(default='Not Set', max_length=250),
        ),
    ]