from django.contrib import admin

# Register your models here.
from apps.urls.models import Urls


@admin.register(Urls)
class UrlsModelAdmin(admin.ModelAdmin):
    list_display = [
        'url',
        'slug',
        'seen_count',
    ]

    class Meta:
        model = Urls