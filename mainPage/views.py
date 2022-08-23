from itertools import repeat

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("메인 페이지 개발 중")

def home(request):
    return render(request, 'home.html')