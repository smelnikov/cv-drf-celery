from django.contrib import admin

from . import models


class VideoInline(admin.TabularInline):
    model = models.VideoContent
    extra = 1


class AudioInline(admin.TabularInline):
    model = models.AudioContent
    extra = 1


class TextInline(admin.TabularInline):
    model = models.TextContent
    extra = 1


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    search_fields = ['^title', '^content__title']
    inlines = [
        VideoInline,
        AudioInline,
        TextInline
    ]
