# Generated by Django 2.2 on 2019-07-12 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190712_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subtopic', to='blog.Topic'),
        ),
    ]