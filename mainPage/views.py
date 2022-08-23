from itertools import repeat

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("메인 페이지 개발 중")

def home(request):
    return render(request, 'home.html')

def god(request):
    return render(request, 'god.html')

def card(request):
    return render(request, 'card.html')

def partner(request):
    return render(request, 'partner.html')

def trio(request):
    return render(request, 'trio.html')

def dual(request):
    return render(request, 'dual.html')
