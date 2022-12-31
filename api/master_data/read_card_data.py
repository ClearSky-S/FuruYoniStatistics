import csv
from api.models import Card, God
with open('card_data.csv', 'r') as csvfile:
    r = csv.reader(csvfile)
    # card_code, god_code, card_name, pick_count, pick_ratio, win_count, win_ratio
    for row in r:
        card = Card()
        card.card_code = row[0]
        card.god_code = row[1]
        card.god_id = God.objects.get(god_code=row[1])
        card.card_name = row[2]
        pick_count, pick_ratio, win_count, win_ratio = 0, 0, 0, 0
