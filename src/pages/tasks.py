from celery import shared_task
from django.db.models import F

from .models import Content


@shared_task
def increase_page_counters(page_id, **kwargs):
    """ Увеличивает счетчик просмотров контента на странице """
    Content.objects.filter(page_id=page_id).update(counter=F('counter') + 1)
