# Generated by Django 4.2.1 on 2023-05-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_channels_channel_url_alter_videos_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channels',
            name='title',
            field=models.CharField(max_length=250, verbose_name='channel_title'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='title',
            field=models.TextField(max_length=250, verbose_name='video_title'),
        ),
    ]
