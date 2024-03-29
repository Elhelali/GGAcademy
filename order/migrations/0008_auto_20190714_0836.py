# Generated by Django 2.2 on 2019-07-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20190713_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='ride',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=None, to='shop.Product'),
        ),
    ]
