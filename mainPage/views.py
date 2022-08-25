from itertools import repeat

from django.shortcuts import render
from django.http import HttpResponse
from api.models import Dual
# Create your views here.


def index(request):
    return HttpResponse("메인 페이지 개발 중")

def home(request):
    return render(request, 'home.html')

def god(request):
    return render(request, 'god.html')

def card_god_select(request):
    return render(request, 'card_god_select.html')

def card(request, god):
    return render(request, 'card.html')

def partner_god_select(request):
    return render(request, 'partner_god_select.html')

def partner(request, god):
    return render(request, 'partner.html')

def trio_god_select_1(request):
    return render(request, 'trio_god_select_1.html')

def trio_god_select_2(request, god1):
    return render(request, 'trio_god_select_2.html')

def trio(request, god1, god2):
    return render(request, 'trio.html')

def dual(request):
    dual_list = Dual.objects.order_by('-time')
    context = {
        'dual_list': dual_list
    }
    return render(request, 'dual.html', context)
def decklist(request, number,isWinner):
    return render(request, 'decklist.html')
