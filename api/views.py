from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    print(request)
    return HttpResponse("api 페이지 개발 중")


def dual_manual_post(request):
    return render(request, 'api_post_dual_manual.html')

@csrf_exempt
def dual(request):
    a = request
    print(a.POST)
    print(type(a))
    # print(a.get("isRank"))
    return HttpResponse(json.dumps(request.POST), content_type="application/json")

@csrf_exempt
def test(request):
    print(request.POST)
    a = {"result": "success"}
    return HttpResponse(json.dumps(a), content_type="application/json")