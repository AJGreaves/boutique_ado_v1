# Generated by Django 3.2.25 on 2025-02-03 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='strip_pid',
            new_name='stripe_pid',
        ),
    ]
