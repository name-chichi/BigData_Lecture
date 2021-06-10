import json
import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from data.adata import Adata
from data.tempa import Tempa


def loginimpl(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    print(id, pwd)
    return render(request, 'jq04.html')


def registerimpl(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    name = request.POST['name']
    age = request.POST['age']
    print(id, pwd, name, age)
    return render(request, 'jq05.html')

def ajs01(request):
    now = time.localtime()
    print(now)
    return HttpResponse(now)

def ajs011(request):
    result = Adata().aj011()
    json_result = json.dumps(result)
    return HttpResponse(json_result, content_type='application/json')

def ajs02(request):
    type = request.GET['type']
    result = Adata().aj02(type)
    json_result = json.dumps(result)
    return HttpResponse(json_result, content_type='application/json')

def ajs03(request):
    country = request.GET['country']
    print(country)
    result = Adata().aj03(country)
    json_result = json.dumps(result)
    return HttpResponse(json_result, content_type='application/json')

def ajs04(request):
    year = int(request.GET['year'])
    month = int(request.GET['month'])
    result = Tempa().seoulam(year, month)
    json_result = json.dumps(result)
    return HttpResponse(json_result, content_type='application/json')