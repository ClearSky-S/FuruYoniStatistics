from itertools import repeat

from django.shortcuts import render
from django.http import HttpResponse
from api.models import Dual, God


# Create your views here.


def index(request):
    return HttpResponse("메인 페이지 개발 중")


def home(request):
    context = {"god_list": God.objects.order_by("-win_ratio")[0:10]}
    return render(request, 'home.html', context)


def god(request, sort_by="win"):
    context = {}
    if sort_by == "win":
        context = {"god_list": God.objects.order_by("-win_ratio")}
    elif sort_by == "pick":
        context = {"god_list": God.objects.order_by("-pick_ratio")}
    elif sort_by == "ban":
        context = {"god_list": God.objects.order_by("-ban_ratio")}

    return render(request, 'god.html', context)


def card_god_select(request):
    context = {"god_list": God.objects.all()}
    return render(request, 'card_god_select.html', context)


def card(request, god):
    return render(request, 'card.html')


def partner_god_select(request):
    context = {"god_list": God.objects.all()}
    return render(request, 'partner_god_select.html', context)


def partner(request, god):
    return render(request, 'partner.html')


def trio_god_select_1(request):
    context = {"god_list": God.objects.all()}
    return render(request, 'trio_god_select_1.html', context)


def trio_god_select_2(request, god1):
    context = {"god_list": God.objects.all()}
    return render(request, 'trio_god_select_2.html', context)


def trio(request, god1, god2):
    return render(request, 'trio.html')


def dual(request):
    dual_list = Dual.objects.order_by('-time')[:50]
    dual_data = []

    for dual_row in dual_list:
        dual_data.append({
            'id': dual_row.pk,
            'time': dual_row.time,

            'winner_name': dual_row.winner_name,
            'winner_god_1': God.objects.get(god_code=dual_row.winner_god_1),
            'winner_god_2': God.objects.get(god_code=dual_row.winner_god_2),
            'winner_god_ban':
                " "
                if dual_row.winner_god_ban == "None"
                else God.objects.get(god_code=dual_row.winner_god_ban),
            'winner_god_1_code': dual_row.winner_god_1,
            'winner_god_2_code': dual_row.winner_god_2,

            'loser_name': dual_row.loser_name,
            'loser_god_1': God.objects.get(god_code=dual_row.loser_god_1),
            'loser_god_2': God.objects.get(god_code=dual_row.loser_god_2),
            'loser_god_ban':
                " "
                if dual_row.loser_god_ban == "None"
                else God.objects.get(god_code=dual_row.loser_god_ban),
            'loser_god_1_code': dual_row.loser_god_1,
            'loser_god_2_code': dual_row.loser_god_2,
        })
    context = {
        'dual_list': dual_data
    }
    return render(request, 'dual.html', context)


def decklist(request, dual_id):
    dual_model = Dual.objects.get(id=dual_id)
    winner_deck_list = [
        dual_model.winner_normal_card_1,
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
    winner_deck_list = map(lambda x: {
        "name": x,
        "code": x,
        "god_code": dual_model.winner_god_1 if dual_model.winner_god_1[:2] == x[:2]
        else dual_model.winner_god_2
    }, winner_deck_list)

    loser_deck_list = [
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
    loser_deck_list = map(lambda x: {
        "name": x,
        "code": x,
        "god_code": dual_model.loser_god_1 if dual_model.loser_god_1[:2] == x[:2]
        else dual_model.loser_god_2
    }, loser_deck_list)

    context = {
        "winner_god1": God.objects.get(god_code=dual_model.winner_god_1),
        "winner_god2": God.objects.get(god_code=dual_model.winner_god_2),
        "winner_god1_code": dual_model.winner_god_1,
        "winner_god2_code": dual_model.winner_god_2,
        "winner_deck_list": winner_deck_list,
        "winner_deck_code": dual_model.winner_deck_code,
        "loser_god1": God.objects.get(god_code=dual_model.loser_god_1),
        "loser_god2": God.objects.get(god_code=dual_model.loser_god_2),
        "loser_god1_code": dual_model.loser_god_1,
        "loser_god2_code": dual_model.loser_god_2,
        "loser_deck_list": loser_deck_list,
        "loser_deck_code": dual_model.loser_deck_code
    }

    return render(request, 'decklist.html', context)
