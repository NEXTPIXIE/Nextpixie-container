# Generated by Django 4.1.7 on 2023-03-17 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('can_create_album', 'Can Create Album'), ('can_view_album', 'Can View Album')]},
        ),
    ]
