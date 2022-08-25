from django.shortcuts import render
from django.http import HttpResponse

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
        data = dict(request.POST)
        print(data)
        print(request.POST.get('aa'))
        return HttpResponse(json.dumps(request.POST), content_type="application/json")


    else:
        return HttpResponse("404")
        

@csrf_exempt
def tabletop(request):
    if request.method == 'POST':
        print(request.POST)
        a = {"result": "success"}
        return HttpResponse(json.dumps(a), content_type="application/json")


