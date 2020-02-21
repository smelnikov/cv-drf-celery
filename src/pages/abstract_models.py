from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import TITLE_MAX_LENGTH


class AbstractContent(models.Model):
    title = models.CharField(_('Заголовок'), max_length=TITLE_MAX_LENGTH)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
