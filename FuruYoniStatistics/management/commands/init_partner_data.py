from django.core.management.base import BaseCommand, CommandError
from api.models import Partner, God


# gdd.json 부터 로드할 것
class Command(BaseCommand):
    help = 'set partyner model'

    def handle(self, *args, **options):
        gods = God.objects.all()

        for god1 in gods:
            print(god1)
            for god2 in gods:
                if god1.pk >= god2.pk:
                    continue
                partner = Partner()
                partner.pick_count = 0
                partner.pick_ratio = 0
                partner.win_count = 0
                partner.win_ratio = 0
                partner.save()
                partner.gods.add(god1)
                partner.gods.add(god2)





