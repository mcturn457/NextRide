# Generated by Django 4.1.3 on 2022-12-18 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scooter_app', '0005_remove_user_email_remove_user_pw_remove_user_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
    ]
