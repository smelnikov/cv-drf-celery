from django.core.management.base import BaseCommand

from pages.models import Page, AudioContent, VideoContent, TextContent
from pages.faker import fake


class Command(BaseCommand):
    help = 'Fill database with demo page objects'

    def handle(self, *args, **options):
        contents = [AudioContent, VideoContent, TextContent]
        self.stdout.write(self.style.SUCCESS('Generating...'))
        for i in range(fake.random_int(max=1000)):
            page = fake.model(Page)
            page.save()

            for pos in range(fake.random_int(max=10)):
                model_cls = contents[fake.random_int(max=len(contents) - 1)]
                fake.model(model_cls, page=page, pos=pos).save()

        self.stdout.write(self.style.SUCCESS('Demo pages created! Have fun!'))
