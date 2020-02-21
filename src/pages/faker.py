from faker import Faker as BaseFaker

from . import TITLE_MAX_LENGTH


class Faker(BaseFaker):
    def title(self):
        return self.sentence()[:TITLE_MAX_LENGTH - 1]

    def file_url(self, category=None, extension=None):
        """
        Args:
             category(str): audio|image|office|text|video
             extension(str): расширение файла
        """
        return self.uri() + self.file_name(category=category, extension=extension)

    def model(self, model_cls, **defaults):
        """
        Args:
             model_cls(django.db.Model): модель данных
             defaults(dict): значения полей по-умолчанию
        """
        defaults['title'] = self.title()

        if model_cls.__name__ == 'AudioContent':
            defaults.update({
                'path': self.file_url(category='audio'),
                'bitrate': self.random_number()
            })
        if model_cls.__name__ == 'VideoContent':
            defaults.update({
                'path': self.file_url(category='video'),
                'subtitle': self.file_url(extension='srt')
            })
        if model_cls.__name__ == 'TextContent':
            defaults.update({
                'value': self.paragraph()
            })

        instance = model_cls(**defaults)

        return instance


fake = Faker()
