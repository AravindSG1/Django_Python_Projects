# Generated by Django 5.1.6 on 2025-05-01 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryagentprofile',
            old_name='user',
            new_name='user_id',
        ),
    ]
