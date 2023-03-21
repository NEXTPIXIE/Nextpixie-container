# Generated by Django 4.1.7 on 2023-03-19 23:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userphotos_album_id_alter_useralbum_caption_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCategories',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='useralbum',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.usercategories'),
        ),
    ]
