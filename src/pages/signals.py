from django.core.signals import Signal
from django.dispatch import receiver

from pages import models, tasks


page_fetched = Signal()


@receiver(page_fetched)
def page_detail_fetched(sender, **kwargs):
    if isinstance(sender, models.Page):
        page_id = sender.pk
        tasks.increase_page_counters.delay(page_id)
