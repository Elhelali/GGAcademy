# Generated by Django 2.2 on 2019-06-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20190624_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
