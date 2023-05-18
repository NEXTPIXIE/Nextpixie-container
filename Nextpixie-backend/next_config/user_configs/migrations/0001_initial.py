# Generated by Django 4.1.7 on 2023-04-25 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('profile_tag', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user_category', models.CharField(blank=True, max_length=200, null=True)),
                ('user_url', models.URLField(blank=True, null=True)),
                ('user_bio', models.CharField(blank=True, max_length=800, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
