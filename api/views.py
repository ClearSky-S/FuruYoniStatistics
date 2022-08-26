from django.shortcuts import render
from django.http import HttpResponse
from .models import Dual, TotalGame, God
import json

from django.utils import timezone


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    print(request)
    return HttpResponse("api 페이지 개발 중")


def dual_manual_post(request):
    return render(request, 'api_post_dual_manual.html')


def dual(request):
    if request.method == 'POST':
        print(request.POST)
        dual_model = Dual()

        dual_model.time = timezone.now()
        dual_model.isRank = request.POST.get('isRank')

        dual_model.winner_name = request.POST.get('winner_name')
        dual_model.winner_god_1 = request.POST.get('winner_god_1')
        dual_model.winner_god_2 = request.POST.get('winner_god_2')
        dual_model.winner_god_ban = request.POST.get('winner_god_ban')
        dual_model.winner_deck_code = request.POST.get('winner_deck_code')

        dual_model.winner_normal_card_1 = request.POST.get('winner_normal_card_1')
        dual_model.winner_normal_card_2 = request.POST.get('winner_normal_card_2')
        dual_model.winner_normal_card_3 = request.POST.get('winner_normal_card_3')
        dual_model.winner_normal_card_4 = request.POST.get('winner_normal_card_4')
        dual_model.winner_normal_card_5 = request.POST.get('winner_normal_card_5')
        dual_model.winner_normal_card_6 = request.POST.get('winner_normal_card_6')
        dual_model.winner_normal_card_7 = request.POST.get('winner_normal_card_7')

        dual_model.winner_special_card_1 = request.POST.get('winner_special_card_1')
        dual_model.winner_special_card_2 = request.POST.get('winner_special_card_2')
        dual_model.winner_special_card_3 = request.POST.get('winner_special_card_3')

        dual_model.loser_name = request.POST.get('loser_name')
        dual_model.loser_god_1 = request.POST.get('loser_god_1')
        dual_model.loser_god_2 = request.POST.get('loser_god_2')
        dual_model.loser_god_ban = request.POST.get('loser_god_ban')
        dual_model.loser_deck_code = request.POST.get('loser_deck_code')

        dual_model.loser_normal_card_1 = request.POST.get('loser_normal_card_1')
        dual_model.loser_normal_card_2 = request.POST.get('loser_normal_card_2')
        dual_model.loser_normal_card_3 = request.POST.get('loser_normal_card_3')
        dual_model.loser_normal_card_4 = request.POST.get('loser_normal_card_4')
        dual_model.loser_normal_card_5 = request.POST.get('loser_normal_card_5')
        dual_model.loser_normal_card_6 = request.POST.get('loser_normal_card_6')
        dual_model.loser_normal_card_7 = request.POST.get('loser_normal_card_7')

        dual_model.loser_special_card_1 = request.POST.get('loser_special_card_1')
        dual_model.loser_special_card_2 = request.POST.get('loser_special_card_2')
        dual_model.loser_special_card_3 = request.POST.get('loser_special_card_3')

        dual_model.save()


        total_game = TotalGame.objects.all()
        if len(total_game)==0:
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
            print(god)
            try:
                god.ban_ratio = round(god.ban_count/god.pick_count*100, 1)
            except ZeroDivisionError:
                god.ban_ratio = 0
            try:
                god.win_ratio = round(god.win_count/(god.pick_count-god.ban_count)*100, 1)
            except ZeroDivisionError:
                god.win_ratio = 0
            god.pick_ratio = round(god.pick_count/total_game*100, 1)
            god.save()



        return HttpResponse(json.dumps(request.POST), content_type="application/json")
    else:
        return HttpResponse("404")
        

@csrf_exempt
def tabletop(request):
    if request.method == 'POST':
        print(request.POST)
        dual_model = Dual()

        dual_model.time = timezone.now()
        dual_model.isRank = request.POST.get('isRank')

        dual_model.winner_name = request.POST.get('winner_name')
        dual_model.winner_god_1 = request.POST.get('winner_god_1')
        dual_model.winner_god_2 = request.POST.get('winner_god_2')
        dual_model.winner_god_ban = request.POST.get('winner_god_ban')
        dual_model.winner_deck_code = request.POST.get('winner_deck_code')

        dual_model.winner_normal_card_1 = request.POST.get('winner_normal_card_1')
        dual_model.winner_normal_card_2 = request.POST.get('winner_normal_card_2')
        dual_model.winner_normal_card_3 = request.POST.get('winner_normal_card_3')
        dual_model.winner_normal_card_4 = request.POST.get('winner_normal_card_4')
        dual_model.winner_normal_card_5 = request.POST.get('winner_normal_card_5')
        dual_model.winner_normal_card_6 = request.POST.get('winner_normal_card_6')
        dual_model.winner_normal_card_7 = request.POST.get('winner_normal_card_7')

        dual_model.winner_special_card_1 = request.POST.get('winner_special_card_1')
        dual_model.winner_special_card_2 = request.POST.get('winner_special_card_2')
        dual_model.winner_special_card_3 = request.POST.get('winner_special_card_3')

        dual_model.loser_name = request.POST.get('loser_name')
        dual_model.loser_god_1 = request.POST.get('loser_god_1')
        dual_model.loser_god_2 = request.POST.get('loser_god_2')
        dual_model.loser_god_ban = request.POST.get('loser_god_ban')
        dual_model.loser_deck_code = request.POST.get('loser_deck_code')

        dual_model.loser_normal_card_1 = request.POST.get('loser_normal_card_1')
        dual_model.loser_normal_card_2 = request.POST.get('loser_normal_card_2')
        dual_model.loser_normal_card_3 = request.POST.get('loser_normal_card_3')
        dual_model.loser_normal_card_4 = request.POST.get('loser_normal_card_4')
        dual_model.loser_normal_card_5 = request.POST.get('loser_normal_card_5')
        dual_model.loser_normal_card_6 = request.POST.get('loser_normal_card_6')
        dual_model.loser_normal_card_7 = request.POST.get('loser_normal_card_7')

        dual_model.loser_special_card_1 = request.POST.get('loser_special_card_1')
        dual_model.loser_special_card_2 = request.POST.get('loser_special_card_2')
        dual_model.loser_special_card_3 = request.POST.get('loser_special_card_3')

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
            print(god)
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

        return HttpResponse(json.dumps(request.POST), content_type="application/json")
    else:
        return HttpResponse("404")
