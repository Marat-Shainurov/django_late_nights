from django.db import models

class MainChannels(models.Model):
    channel_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250)
    views = models.IntegerField()
    subscribers = models.IntegerField()
    videos = models.IntegerField()
    channel_url = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        managed = False
        db_table = 'channels'


class MainVideos(models.Model):
    video_id = models.BigAutoField(primary_key=True)
    title = models.TextField(verbose_name='video_title')
    publish_date = models.DateTimeField()
    video_url = models.CharField(max_length=255)
    channel = models.ForeignKey(MainChannels, models.DO_NOTHING, to_field='channel_id')

    def __str__(self):
        return '{0} {1} {2}'.format(self.video_id, self.title, self.video_url)

    class Meta:
        managed = False
        db_table = 'videos'
