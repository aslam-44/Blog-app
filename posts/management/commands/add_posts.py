from django.core.management.base import BaseCommand
from posts.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Deleting all Data...")
Category.objects.all().delete()
Author.objects.all().delete()
Post.objects.all().delete()