from django.db import models

# Create your models here.


class Dual(models.Model):
    time = 0
    isRank = 0

    winner_name = 0
    winner_god1 = 0
    winner_god2 = 0
    winner_normal_card1 = 0
    winner_normal_card2 = 0
    winner_normal_card3 = 0
    winner_normal_card4 = 0
    winner_normal_card5 = 0
    winner_normal_card6 = 0
    winner_normal_card7 = 0
    winner_special_card1 = 0
    winner_special_card2 = 0
    winner_special_card3 = 0

    loser_name = 0
    loser_god1 = 0
    loser_god2 = 0
    loser_normal_card1 = 0
    loser_normal_card2 = 0
    loser_normal_card3 = 0
    loser_normal_card4 = 0
    loser_normal_card5 = 0
    loser_normal_card6 = 0
    loser_normal_card7 = 0
    loser_special_card1 = 0
    loser_special_card2 = 0
    loser_special_card3 = 0


class God(models.Model):
    god_code = 0
    god_name = 0

    pick_count = 0
    ban_count = 0
    use_count = 0
    win_count = 0

    # all gods


class Card(models.Model):
    card_code = models.CharField(max_length=200)
    god = 0

    use_count = 0
    win_count = 0

