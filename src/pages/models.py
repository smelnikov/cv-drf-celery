from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.managers import InheritanceManager

from . import abstract_models


class Page(abstract_models.AbstractContent):
    class Meta:
        verbose_name = _('Страница')
        verbose_name_plural = _('Страницы')


class Content(abstract_models.AbstractContent):
    page = models.ForeignKey(Page, related_name='content', on_delete=models.CASCADE)
    pos = models.IntegerField(_('№п/п'), default=0, blank=True)
    counter = models.IntegerField(_('Счётчик просмотров'), default=0, editable=False, blank=True)

    objects = InheritanceManager()

    class Meta:
        ordering = ('page', 'pos')
        verbose_name = _('Контент')
        verbose_name_plural = _('Контент')


class AudioContent(Content):
    path = models.URLField(_('Ссылка на аудиофайл'))
    bitrate = models.IntegerField(_('Битрейт'), help_text='бит в секунду')

    class Meta:
        verbose_name = _('Аудио')
        verbose_name_plural = _('Аудио')


class VideoContent(Content):
    path = models.URLField(_('Ссылка на видеофайл'))
    subtitle = models.URLField(_('Ссылка на файл субтитров'))

    class Meta:
        verbose_name = _('Видео')
        verbose_name_plural = _('Видео')


class TextContent(Content):
    value = models.TextField(_('Описание'))

    class Meta:
        verbose_name = _('Текст')
        verbose_name_plural = _('Текст')
