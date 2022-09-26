from django.shortcuts import render
from django.http import HttpResponse
from .models import Dual, TotalGame, God, Card, Partner
import json

from django.utils import timezone

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    print(request)
    return HttpResponse("api 페이지 개발 중")


def dual_manual_post(request):
    return render(request, 'api_post_dual_manual.html')


@csrf_exempt
def tabletop(request):
    try:
        if request.method == 'POST':
            # print(request.POST)
            try:
                God.objects.get(god_code=request.POST.get('winner_god_1'))
                God.objects.get(god_code=request.POST.get('winner_god_2'))
                God.objects.get(god_code=request.POST.get('loser_god_1'))
                God.objects.get(god_code=request.POST.get('loser_god_2'))
                if request.POST.get('winner_god_ban') != "None":
                    God.objects.get(god_code=request.POST.get('winner_god_ban'))
                if request.POST.get('loser_god_ban') != "None":
                    God.objects.get(god_code=request.POST.get('loser_god_ban'))
            except Exception:
                return HttpResponse('Wrong god code')

            dual_model = Dual()
            if request.POST.get('winner_isPublic') == None:
                dual_model.winner_isPublic = True
            else:
                dual_model.winner_isPublic = request.POST.get('winner_isPublic')
            if request.POST.get('loser_isPublic') == None:
                dual_model.loser_isPublic = True
            else:
                dual_model.loser_isPublic = request.POST.get('loser_isPublic')
            dual_model.time = timezone.now()
            dual_model.isRank = request.POST.get('isRank')

            dual_model.winner_name = request.POST.get('winner_name')
            dual_model.winner_god_1 = request.POST.get('winner_god_1')
            dual_model.winner_god_2 = request.POST.get('winner_god_2')
            dual_model.winner_god_ban = request.POST.get('winner_god_ban')
            dual_model.winner_deck_code = request.POST.get('winner_deck_code')

            dual_model.winner_normal_card_1 = request.POST.get('winner_normal_card_1').upper()
            dual_model.winner_normal_card_2 = request.POST.get('winner_normal_card_2').upper()
            dual_model.winner_normal_card_3 = request.POST.get('winner_normal_card_3').upper()
            dual_model.winner_normal_card_4 = request.POST.get('winner_normal_card_4').upper()
            dual_model.winner_normal_card_5 = request.POST.get('winner_normal_card_5').upper()
            dual_model.winner_normal_card_6 = request.POST.get('winner_normal_card_6').upper()
            dual_model.winner_normal_card_7 = request.POST.get('winner_normal_card_7').upper()

            dual_model.winner_special_card_1 = request.POST.get('winner_special_card_1').upper()
            dual_model.winner_special_card_2 = request.POST.get('winner_special_card_2').upper()
            dual_model.winner_special_card_3 = request.POST.get('winner_special_card_3').upper()

            dual_model.loser_name = request.POST.get('loser_name')
            dual_model.loser_god_1 = request.POST.get('loser_god_1')
            dual_model.loser_god_2 = request.POST.get('loser_god_2')
            dual_model.loser_god_ban = request.POST.get('loser_god_ban')
            dual_model.loser_deck_code = request.POST.get('loser_deck_code')

            dual_model.loser_normal_card_1 = request.POST.get('loser_normal_card_1').upper()
            dual_model.loser_normal_card_2 = request.POST.get('loser_normal_card_2').upper()
            dual_model.loser_normal_card_3 = request.POST.get('loser_normal_card_3').upper()
            dual_model.loser_normal_card_4 = request.POST.get('loser_normal_card_4').upper()
            dual_model.loser_normal_card_5 = request.POST.get('loser_normal_card_5').upper()
            dual_model.loser_normal_card_6 = request.POST.get('loser_normal_card_6').upper()
            dual_model.loser_normal_card_7 = request.POST.get('loser_normal_card_7').upper()

            dual_model.loser_special_card_1 = request.POST.get('loser_special_card_1').upper()
            dual_model.loser_special_card_2 = request.POST.get('loser_special_card_2').upper()
            dual_model.loser_special_card_3 = request.POST.get('loser_special_card_3').upper()

            dual_model.save()

            total_game = TotalGame.objects.all()
            if len(total_game) == 0:
                total_game = TotalGame()
                total_game.total = 1
                total_game.save()
            else:
                total_game = total_game[0]
                total_game.total += 1
                total_game.save()
            total_game = total_game.total

            for winner_god in [dual_model.winner_god_1, dual_model.winner_god_2]:
                winner_god = God.objects.get(god_code=winner_god)
                winner_god.pick_count += 1
                winner_god.win_count += 1
                winner_god.save()

            for loser_god in [dual_model.loser_god_1, dual_model.loser_god_2]:
                loser_god = God.objects.get(god_code=loser_god)
                loser_god.pick_count += 1
                loser_god.save()

            for baned_god in [dual_model.winner_god_ban, dual_model.loser_god_ban]:
                if baned_god == "None":
                    break
                baned_god = God.objects.get(god_code=baned_god)
                baned_god.pick_count += 1
                baned_god.ban_count += 1
                baned_god.save()

            for god in God.objects.all():
                try:
                    god.ban_ratio = round(god.ban_count / god.pick_count * 100, 1)
                except ZeroDivisionError:
                    god.ban_ratio = 0
                try:
                    god.win_ratio = round(god.win_count / (god.pick_count - god.ban_count) * 100, 1)
                except ZeroDivisionError:
                    god.win_ratio = 0
                god.pick_ratio = round(god.pick_count / total_game * 100, 1)
                god.save()

            winner_card_list = [
                dual_model.winner_normal_card_1,  # card code
                dual_model.winner_normal_card_2,
                dual_model.winner_normal_card_3,
                dual_model.winner_normal_card_4,
                dual_model.winner_normal_card_5,
                dual_model.winner_normal_card_6,
                dual_model.winner_normal_card_7,
                dual_model.winner_special_card_1,
                dual_model.winner_special_card_2,
                dual_model.winner_special_card_3,
            ]
            loser_card_list = [
                dual_model.loser_normal_card_1,
                dual_model.loser_normal_card_2,
                dual_model.loser_normal_card_3,
                dual_model.loser_normal_card_4,
                dual_model.loser_normal_card_5,
                dual_model.loser_normal_card_6,
                dual_model.loser_normal_card_7,
                dual_model.loser_special_card_1,
                dual_model.loser_special_card_2,
                dual_model.loser_special_card_3,
            ]

            for card in winner_card_list:
                god1, god2 = dual_model.winner_god_1, dual_model.winner_god_2
                god = god1 if card[:2] == god1[:2] else god2
                card = Card.objects.get(card_code=card.upper(), god_code=god)
                card.win_count += 1
                card.pick_count += 1
                card.save()

            for card in loser_card_list:
                god1, god2 = dual_model.loser_god_1, dual_model.loser_god_2
                god = god1 if card[:2] == god1[:2] else god2
                card = Card.objects.get(card_code=card.upper(), god_code=god)
                card.pick_count += 1
                card.save()

            for god in [dual_model.winner_god_1, dual_model.winner_god_2, dual_model.loser_god_1, dual_model.loser_god_2]:
                card_list = Card.objects.filter(god_code=god)
                god = God.objects.get(god_code=god)
                for card in card_list:
                    try:
                        card.win_ratio = card.win_count / card.pick_count * 100
                    except ZeroDivisionError:
                        card.win_ratio = 0
                    try:
                        card.pick_ratio = card.pick_count / (god.pick_count - god.ban_count) * 100
                    except ZeroDivisionError:
                        card.pick_ratio = 0
                    card.save()

            winner_partner = Partner.objects.filter(gods__god_code=dual_model.winner_god_1).filter(gods__god_code=dual_model.winner_god_2)[0]
            winner_partner.win_count += 1
            winner_partner.pick_count += 1
            winner_partner.save()

            loser_partner = Partner.objects.filter(gods__god_code=dual_model.loser_god_1).filter(gods__god_code=dual_model.loser_god_2)[0]
            loser_partner.pick_count += 1
            loser_partner.save()

            for partner in Partner.objects.all():
                try:
                    partner.win_ratio = partner.win_count / partner.pick_count * 100
                except ZeroDivisionError:
                    partner.win_ratio = 0
                try:
                    partner.pick_ratio = partner.pick_count / TotalGame.objects.all()[0].total * 100
                except ZeroDivisionError:
                    partner.pick_ratio = 0
                partner.save()

            return HttpResponse(json.dumps(request.POST), content_type="application/json")
        else:
            return HttpResponse("404")
    except Exception:
        pass

def test(request):
    print(request.POST.get("aa"))