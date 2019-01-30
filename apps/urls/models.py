from django.contrib.auth.models import User
from django.db import models


class Urls(models.Model):
    url = models.URLField(unique=True)
    slug = models.CharField(unique=True, null=False, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seen_count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = "Urls"