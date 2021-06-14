import json
import logging
import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from analysis.MyAnalysis import MyAnalysis

user_logger = logging.getLogger('users')
item_logger = logging.getLogger('items')
iot_logger = logging.getLogger('iot_file')

def ws(request):
    year = request.GET['year'];
    month = request.GET['month'];
    result = MyAnalysis().wm(int(year),int(month));
    return HttpResponse(json.dumps(result),content_type='application/json');

def ages(request):
    target = request.GET['target']
    result = MyAnalysis().localage(target)
    # print(result)
    return HttpResponse(json.dumps(result),content_type='application/json')

def genders(request):
    target = request.GET['target']
    result = MyAnalysis().genderage(target)
    # print(result)
    return HttpResponse(json.dumps(result),content_type='application/json')

def genders2(request):
    target = request.GET['target']
    result = MyAnalysis().genderage2(target)
    # print(result)
    return HttpResponse(json.dumps(result),content_type='application/json')

def iots(request):
    speed = request.GET['speed']
    rpm = request.GET['rpm']
    temp = request.GET['temp']
    t = time.localtime()
    now = str(t.tm_year)+'-'+str(t.tm_mon)+'-'+str(t.tm_mday)+'-'+str(t.tm_hour)+'-'+str(t.tm_min)+'-'+str(t.tm_sec)
    iot_logger.debug(speed + ',' + rpm + ',' + temp)
    # print(now,speed, rpm, temp);
    return render(request, 'ok.html')
