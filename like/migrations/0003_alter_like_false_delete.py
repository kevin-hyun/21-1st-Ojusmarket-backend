# Generated by Django 3.2.4 on 2021-06-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    
    dependencies = [
        ('like', '0002_like_false_delete'),
    ]
    
    operations = [
        migrations.AlterField(
            model_name='like',
            name='false_delete',
            field=models.BooleanField(default=False),
        ),
    ]
    