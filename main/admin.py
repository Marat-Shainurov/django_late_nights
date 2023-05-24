from django.contrib import admin

from main.models import MainChannels, MainVideos


@admin.register(MainChannels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ('channel_id', 'title', 'views', 'subscribers', 'videos', 'channel_url')
    list_filter = ('title', 'channel_id')


@admin.register(MainVideos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('channel', 'title', 'video_id', 'publish_date', 'video_url')
    list_filter = ('publish_date',)
    search_fields = ('title',)
