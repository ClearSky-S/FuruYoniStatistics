import re
from itertools import repeat


from django.shortcuts import render
from django.http import HttpResponse
from django.utils import http

from api.models import Dual, God, Card, Partner
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


def index(request):
    return HttpResponse("메인 페이지 개발 중")


def home(request):
    context = {
        "god_list": God.objects.order_by("-pick_ratio")[0:10],
        "card_list": Card.objects.order_by("-pick_ratio")[0:10]
    }
    return render(request, 'home.html', context)


def god(request, sort_by="pick"):
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


def card(request, god_code):
    god_code = God.objects.get(god_code=god_code.upper())
    card_list = Card.objects.filter(god=god_code)
    context = {
        "god": god_code,
        "card_list": card_list
    }
    return render(request, 'card.html', context)


def partner_god_select(request):
    context = {"god_list": God.objects.all()}
    return render(request, 'partner_god_select.html', context)


def partner(request, god_code, sort_by="pick"):
    if sort_by == "win":
        partner_list = Partner.objects.filter(gods__god_code=god_code.upper()).order_by("-win_ratio")
    else:
        partner_list = Partner.objects.filter(gods__god_code=god_code.upper()).order_by("-pick_ratio")
    god_list = []
    for partner in partner_list:
        partner_god = partner.gods.all()[0] if partner.gods.all()[0].god_code != god_code else partner.gods.all()[1]
        god_list.append({
            "god_name": partner_god.god_name,
            "pick_ratio": partner.pick_ratio,
            "win_ratio": partner.win_ratio,
            "god_code": partner_god.god_code
        })
    context = {
        "god": God.objects.get(god_code=god_code.upper()),
        "god_list": god_list,
    }
    partner_list = Partner.objects.filter(gods__god_code=god_code).order_by('-pick_ratio')

    return render(request, 'partner.html', context)


def trio_god_select_1(request):
    context = {"god_list": God.objects.all()}
    return render(request, 'trio_god_select_1.html', context)


def trio_god_select_2(request, god_code_1):
    context = {
        "god_list": God.objects.exclude(god_code__contains=god_code_1.upper()[:2]),
        "god1": God.objects.get(god_code=god_code_1.upper())
    }
    return render(request, 'trio_god_select_2.html', context)


def trio(request, god_code_1, god_code_2, sort_by):
    god_code_1 = god_code_1.upper()
    god_code_2 = god_code_2.upper()

    god1 = God.objects.get(god_code=god_code_1)
    god2 = God.objects.get(god_code=god_code_2)
    god_list = God.objects.exclude(god_code__contains=god_code_1[:2]).exclude(god_code__contains=god_code_2[:2])
    trio_list = []
    for god in god_list:
        partner1 = Partner.objects.filter(gods__god_code=god_code_1).filter(gods=god)
        partner2 = Partner.objects.filter(gods__god_code=god_code_2).filter(gods=god)
        trio_list.append({
            "god": god,
            "avg_win_ratio": (partner1[0].win_ratio + partner2[0].win_ratio) / 2,
            "avg_pick_ratio": (partner1[0].pick_ratio + partner2[0].pick_ratio) / 2,
        })
    if sort_by == "win":
        trio_list.sort(key=lambda x: x["avg_win_ratio"], reverse=True)
    else:
        trio_list.sort(key=lambda x: x["avg_pick_ratio"], reverse=True)
    context = {
        "god1": god1,
        "god2": god2,
        "trio_list": trio_list,
    }
    return render(request, 'trio.html', context)


def dual(request):
    def formatPlayerName(name: str):
        def isKorean(text):
            hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
            result = hangul.findall(text)
            return len(result)

        if isKorean(name):
            if len(name) > 8:
                return name[0:8] + "..."
        else:
            if len(name) > 12:
                return name[0:12] + "..."
        return name

    # return HttpResponse("새 시즌이 시작되어 서버 점검중입니다.")
    print(request.GET)
    god1 = request.GET.get('god1', '')
    god2 = request.GET.get('god2', '')
    player = request.GET.get('player', '')
    page = request.GET.get('page', '1')
    dual_list = Dual.objects.all().order_by('-id')
    if god1 != '' and god2 != '':
        try:
            god_code1 = God.objects.get(god_code=god1).god_code
            god_code2 = God.objects.get(god_code=god2).god_code
            dual_list = dual_list.filter((Q(winner_god_1=god_code1)&Q(winner_god_2=god_code2))|(Q(winner_god_1=god_code2)&Q(winner_god_2=god_code1))
                                       |(Q(loser_god_1=god_code1)&Q(loser_god_2=god_code2))|(Q(loser_god_1=god_code2)&Q(loser_god_2=god_code1)))
        except:
            dual_list = dual_list.filter(winner_god_1="none")
    elif god1 != '' or god2 != '':
        try:
            god_code = ''
            if(god1 != ''):
                god_code = God.objects.get(god_code=god1).god_code
            else:
                god_code = God.objects.get(god_code=god2).god_code
            dual_list = dual_list.filter(Q(winner_god_1=god_code)|Q(winner_god_2=god_code)|Q(loser_god_1=god_code)|Q(loser_god_2=god_code))
        except:
            dual_list = dual_list.filter(winner_god_1="none")
    if player:
        dual_list = dual_list.filter(Q(winner_name=player)|Q(loser_name=player))
    # dual_list = Dual.objects.filter(Q(winner_name=player)|Q(loser_name=player)).order_by('-time')\

    paginator = Paginator(dual_list, 20)
    paginator = paginator.get_page(page)

    dual_data = []

    for dual_row in paginator:
        try:
            God.objects.get(god_code=dual_row.winner_god_1)
            God.objects.get(god_code=dual_row.winner_god_2)
            God.objects.get(god_code=dual_row.loser_god_1)
            God.objects.get(god_code=dual_row.loser_god_2)
            if dual_row.winner_god_ban != "None":
                God.objects.get(god_code=dual_row.winner_god_ban)
            if dual_row.loser_god_ban != "None":
                God.objects.get(god_code=dual_row.loser_god_ban)
        except Exception:
            continue

        dual_data.append({
            'id': dual_row.pk,
            'time': dual_row.time,
            'winner_isPublic': dual_row.winner_isPublic,
            'loser_isPublic': dual_row.loser_isPublic,

            'winner_name': formatPlayerName(dual_row.winner_name),
            'winner_god_1': God.objects.get(god_code=dual_row.winner_god_1),
            'winner_god_2': God.objects.get(god_code=dual_row.winner_god_2),
            'winner_god_ban':
                " "
                if dual_row.winner_god_ban == "None"
                else God.objects.get(god_code=dual_row.winner_god_ban),
            'winner_god_1_code': dual_row.winner_god_1,
            'winner_god_2_code': dual_row.winner_god_2,

            'loser_name': formatPlayerName(dual_row.loser_name),
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
        'dual_list': dual_data,
        'paginator': paginator,
        'god1':god1,
        'god2':god2,
        'god_list': God.objects.all(),
        'player':player,
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
        "name": Card.objects.filter(card_code=x)[0].card_name,
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
        "name": Card.objects.filter(card_code=x)[0].card_name,
        "code": x,
        "god_code": dual_model.loser_god_1 if dual_model.loser_god_1[:2] == x[:2]
        else dual_model.loser_god_2
    }, loser_deck_list)

    context = {
        "dual": dual_model,
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


def archive(request):
    context = {}
    return render(request, 'archive.html', context)
