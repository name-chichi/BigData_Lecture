import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from analysis.MyAnalysis import MyAnalysis


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