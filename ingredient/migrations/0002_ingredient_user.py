# Generated by Django 3.2.4 on 2021-06-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('like', '0001_initial'),
        ('ingredient', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='user',
            field=models.ManyToManyField(through='like.Like', to='user.User'),
        ),
    ]
