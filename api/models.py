from django.db import models

# Create your models here.


class Dual(models.Model):
    time = 0
    isRank = 0

    winner_name = 0
    winner_god1 = 0
    winner_god2 = 0
    winner_normal_card_list = 0
    winner_special_card_list = 0

    loser_name = 0
    loser_god1 = 0
    loser_god2 = 0
    loser_normal_card_list = 0
    loser_special_card_list = 0



class God(models.Model):
    god_code = 0
    # saine-O
    # saine-A1
    god_name = 0
    # 「제 2장」 사이네

    pick_count = 0
    pick_ratio = 0
    ban_count = 0
    ban_ratio = 0
    win_count = 0
    win_ratio = 0
    # win / (pick-ban)

class Partner(models.Model):
    pick_count_saine_O = 0
    win_count_saine_O = 0


class Card(models.Model):
    card_code = models.CharField(max_length=200)
    god = 0
    god2 = 0
    god3 = 0

    use_count = 0
    use_rate = 0
    use_count2 = 0
    use_rate = 0
    use_count3 = 0
    use_rate = 0

    win_count = 0
    win_rate = 0
    win_count2 = 0
    win_rate2 = 0
    win_count3 = 0
    win_rate3 = 0

