  # Generated by Django 3.2.4 on 2021-06-14 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cart_id',
            new_name='cart',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='status_id',
            new_name='status',
        ),
    ]