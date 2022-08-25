from django import forms
from api.models import Dual


class DualForm(forms.ModelForm):
    class Meta:
        model = Dual  # 사용할 모델
        fields = ['isRank',
                  'winner_name',
                  'winner_god_1',
                  'winner_god_2',
                  'winner_god_ban',
                  'winner_deck_code',
                  'winner_normal_card_1',
                  'winner_normal_card_2',
                  'winner_normal_card_3',
                  'winner_normal_card_4',
                  'winner_normal_card_5',
                  'winner_normal_card_6',
                  'winner_normal_card_7',
                  'winner_special_card_1',
                  'winner_special_card_2',
                  'winner_special_card_3',
                  'loser_name',
                  'loser_god_1',
                  'loser_god_2',
                  'loser_god_ban',
                  'loser_deck_code',
                  'loser_normal_card_1',
                  'loser_normal_card_2',
                  'loser_normal_card_3',
                  'loser_normal_card_4',
                  'loser_normal_card_5',
                  'loser_normal_card_6',
                  'loser_normal_card_7',
                  'loser_special_card_1',
                  'loser_special_card_2',
                  'loser_special_card_3',
                  ]  # QuestionForm에서 사용할 Question 모델의 속성