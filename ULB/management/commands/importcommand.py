from ULB.models import ULBdata, Dataset
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **options):
        pk = int(options['pk'])
        dataset = Dataset.objects.get(id=pk)
        filename = str(settings.MEDIA_ROOT) + '/'+ str(dataset.File.name)
        insert_count = ULBdata.objects.from_csv(filename, delimiter=';')
        dataset.delete()