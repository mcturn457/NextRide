# Generated by Django 4.1.3 on 2023-01-12 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scooter_app', '0006_remove_user_firstname_remove_user_lastname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='post_code',
            new_name='postalcode',
        ),
        migrations.RemoveField(
            model_name='company',
            name='country',
        ),
        migrations.RemoveField(
            model_name='company',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='company',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='company',
            name='website',
        ),
    ]
