from django.db import models


class Channels(models.Model):
    channel_id = models.IntegerField(primary_key=True, verbose_name='channel_id')
    title = models.CharField(max_length=100, verbose_name='channel_title')
    views = models.IntegerField(verbose_name='channel_views')
    subscribers = models.IntegerField(verbose_name='channel_subscribers')
    videos_number = models.IntegerField(verbose_name='videos_number')
    channel_url = models.URLField(verbose_name='channel_url')

    def __str__(self):
        return f'{self.channel_id} {self.title} {self.channel_url}'

    class Meta:
        verbose_name = 'channel'
        verbose_name_plural = 'channels'


class Videos(models.Model):
    video_id = models.IntegerField(verbose_name='video_id')
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE, to_field='channel_id', verbose_name='channel_id')
    title = models.TextField(verbose_name='video_title')
    publish_date = models.DateTimeField(verbose_name='publish_date')
    video_url = models.IntegerField(verbose_name='video_url')

    def __str__(self):
        return '{0} {1} {2}'.format(self.video_id, self.title, self.video_url)
