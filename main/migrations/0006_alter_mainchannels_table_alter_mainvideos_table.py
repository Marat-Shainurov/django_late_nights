# Generated by Django 4.2.1 on 2023-05-24 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_mainchannels_mainvideos_remove_videos_channel_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='mainchannels',
            table='channels',
        ),
        migrations.AlterModelTable(
            name='mainvideos',
            table='videos',
        ),
    ]
