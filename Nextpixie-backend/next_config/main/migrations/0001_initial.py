# Generated by Django 4.1.7 on 2023-05-26 22:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAlbum',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('date', models.CharField(blank=True, max_length=200, null=True)),
                ('caption', models.TextField()),
                ('album_tag', models.CharField(max_length=200)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPhotos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('album_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='main.useralbum')),
            ],
        ),
    ]
