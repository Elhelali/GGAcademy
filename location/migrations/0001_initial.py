# Generated by Django 2.2 on 2019-06-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
            options={
                'db_table': 'locations',
                'ordering': ['longitude'],
            },
        ),
    ]