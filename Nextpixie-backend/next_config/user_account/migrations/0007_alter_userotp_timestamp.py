# Generated by Django 4.1.7 on 2023-04-02 22:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0006_alter_userotp_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
