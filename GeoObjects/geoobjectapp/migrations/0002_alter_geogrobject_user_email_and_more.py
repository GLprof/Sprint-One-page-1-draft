# Generated by Django 4.2.16 on 2024-11-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoobjectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geogrobject',
            name='user_email',
            field=models.EmailField(max_length=256),
        ),
        migrations.AlterField(
            model_name='geogrobject',
            name='user_name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
