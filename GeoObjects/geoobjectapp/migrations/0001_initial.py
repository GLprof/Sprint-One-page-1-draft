# Generated by Django 4.2.16 on 2024-11-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeogrObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_object', models.CharField(max_length=128)),
                ('latitude_object', models.FloatField()),
                ('longitude_object', models.FloatField()),
                ('height_object', models.FloatField()),
                ('photo_object', models.ImageField(upload_to='')),
                ('user_name', models.CharField(max_length=128)),
                ('user_email', models.EmailField(max_length=256, unique=True)),
                ('user_phone', models.CharField(max_length=128)),
            ],
        ),
    ]
