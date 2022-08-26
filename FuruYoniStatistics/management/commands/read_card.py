from django.core.management.base import BaseCommand, CommandError
import csv
from api.models import Card, God

# gdd.json 부터 로드할 것
class Command(BaseCommand):
    help = 'set card model'

    def handle(self, *args, **options):
        with open('api/master_data/card_data.csv', 'r') as csvfile:
            r = csv.reader(csvfile)
            # card_code, god_code, card_name, pick_count, pick_ratio, win_count, win_ratio
            for row in r:
                if row[0] == 'card_code':
                    continue
                card = Card()
                card.card_code = row[0]
                card.god_code = row[1]
                card.god_id = God.objects.get(god_code=row[1])
                card.card_name = row[2]
                card.pick_count, card.pick_ratio, card.win_count, card.win_ratio = 0, 0, 0, 0
                card.save()
                print(card)
