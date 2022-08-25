from django.db import models


class Dual(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    isRank = models.BooleanField()

    winner_name = models.CharField(max_length=50)
    winner_god_1 = models.CharField(max_length=20)
    winner_god_2 = models.CharField(max_length=20)
    winner_god_ban = models.CharField(max_length=20)
    winner_deck_code = models.CharField(max_length=30)

    winner_normal_card_1 = models.CharField(max_length=20)
    winner_normal_card_2 = models.CharField(max_length=20)
    winner_normal_card_3 = models.CharField(max_length=20)
    winner_normal_card_4 = models.CharField(max_length=20)
    winner_normal_card_5 = models.CharField(max_length=20)
    winner_normal_card_6 = models.CharField(max_length=20)
    winner_normal_card_7 = models.CharField(max_length=20)

    winner_special_card_1 = models.CharField(max_length=20)
    winner_special_card_2 = models.CharField(max_length=20)
    winner_special_card_3 = models.CharField(max_length=20)

    loser_name = models.CharField(max_length=50)
    loser_god_1 = models.CharField(max_length=20)
    loser_god_2 = models.CharField(max_length=20)
    loser_god_ban = models.CharField(max_length=20)
    loser_deck_code = models.CharField(max_length=30)

    loser_normal_card_1 = models.CharField(max_length=20)
    loser_normal_card_2 = models.CharField(max_length=20)
    loser_normal_card_3 = models.CharField(max_length=20)
    loser_normal_card_4 = models.CharField(max_length=20)
    loser_normal_card_5 = models.CharField(max_length=20)
    loser_normal_card_6 = models.CharField(max_length=20)
    loser_normal_card_7 = models.CharField(max_length=20)

    loser_special_card_1 = models.CharField(max_length=20)
    loser_special_card_2 = models.CharField(max_length=20)
    loser_special_card_3 = models.CharField(max_length=20)

    def __str__(self):
        return "대전기록" + str(self.time)

"""

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

"""