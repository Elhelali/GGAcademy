# Generated by Django 2.2 on 2019-06-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20190629_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='place_id',
            field=models.CharField(default='none', max_length=250),
        ),
    ]
