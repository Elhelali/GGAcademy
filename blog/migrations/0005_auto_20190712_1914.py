# Generated by Django 2.2 on 2019-07-12 19:14

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('blog', '0004_auto_20190712_1833'),
    ]
    

    operations = [
  

        migrations.AlterModelOptions(
            name='subtopic',
            options={'ordering': ['topic', 'number']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['post', 'number']},
            
        ),
        migrations.AlterModelTable(
            name='subtopic',
            table='Subtopic',
        ),
        migrations.AlterModelTable(
            name='topic',
            table='Topic',
            
        ),
        
    ]