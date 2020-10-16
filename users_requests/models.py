from django.db import models


class Request(models.Model):
    SERVICE_TYPE = (
        ('Веб сайт', 'Веб сайт'),
        ('Мобильное приложение', 'Мобильное приложение'),
        ('Видео съемка', 'Виде съемка'),
        ('Рекламная продукция', 'Рекламная продукция'),
        ('Услуги дизайна', 'Услуги дизайна'),
        ('Медиа продвижение', 'Медиа продвижение'),
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company_name = models.CharField(max_length=64)
    company_activity = models.TextField(max_length=256)
    phone = models.CharField(max_length=64)
    email = models.EmailField()
    service_type = models.CharField(choices=SERVICE_TYPE, max_length=128)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
