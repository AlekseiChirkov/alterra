from django.db import models
from multiselectfield import MultiSelectField


class Recommendation(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField(max_length=256)
    url = models.URLField(max_length=512, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    bg_image = models.ImageField(default=None)

    def __str__(self):
        return self.title


class Request(models.Model):
    SERVICE_TYPES = (
        ('WEB сайт', 'WEB сайт'),
        ('Моб. приложение', 'Моб. приложение'),
        ('Фото/Видео съемка', 'Фото/Видео съемка'),
        ('Услуги дизайна', 'Услуги дизайна'),
        ('Рекламная продукция', 'Рекламная продукция'),
        ('SMM-продвижение', 'SMM-продвижение'),
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.EmailField()
    company_name = models.CharField(max_length=128)
    company_activity = models.TextField(max_length=128)
    service_types = MultiSelectField(choices=SERVICE_TYPES, max_choices=6, max_length=256)
