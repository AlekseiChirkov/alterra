from django.db import models


class Recommendation(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField(max_length=256)
    url = models.URLField(max_length=512, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    bg_image = models.ImageField(default=None)

    def __str__(self):
        return self.title
