# Generated by Django 2.2 on 2019-06-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20190623_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('discount', models.IntegerField()),
            ],
            options={
                'db_table': 'Coupon',
            },
        ),
    ]