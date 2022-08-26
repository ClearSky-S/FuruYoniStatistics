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


class TotalGame(models.Model):
    total = models.IntegerField()


class God(models.Model):
    # 02-O
    # 02-A1
    god_code = models.CharField(max_length=20)
    # 「제 2장」 사이네
    god_name = models.CharField(max_length=20)
    # 팔상
    god_keyword = models.CharField(max_length=10)
    # 당신의 오라가 1 이하라면...
    god_text = models.CharField(max_length=200)

    pick_count = models.IntegerField()
    # pick / total
    pick_ratio = models.DecimalField(max_digits=4, decimal_places=1)

    ban_count = models.IntegerField()
    # ban / pick
    ban_ratio = models.DecimalField(max_digits=4, decimal_places=1)

    win_count = models.IntegerField()
    # win / (pick-ban)
    win_ratio = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.god_name


"""
class Partner(models.Model):
    pick_count_saine_O = 0
    win_count_saine_O = 0

"""

class Card(models.Model):
    # card_code,god_code,card_name,pick_count,pick_ratio,win_count,win_ratio
    card_code = models.CharField(max_length=200)
    god_code = models.CharField(max_length=20)
    god = models.ForeignKey(God, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=50)
    pick_count = models.IntegerField()
    pick_ratio = models.DecimalField(max_digits=4, decimal_places=1)
    win_count = models.IntegerField()
    win_ratio = models.DecimalField(max_digits=4, decimal_places=1)
    def __str__(self):
        return self.card_name + '(' + self.card_code + ')'


