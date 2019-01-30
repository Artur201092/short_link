from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', type=int)

    def handle(self, *args, **kwargs):
        results = requests.get('https://randomuser.me/api/?results=%s' %kwargs['total']).json()['results']
        for user in results:
            user, created = User.objects.get_or_create(
                username=user['login']['username'],
                password=user['login']['password'],
                first_name=user['name']['first'],
                last_name=user['name']['last'],
                email=user['email'],
                date_joined=user['registered']['date'])
            if created:
                continue
