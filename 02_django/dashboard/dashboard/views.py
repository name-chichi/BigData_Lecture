import json
import time

from django.http import HttpResponse
from django.shortcuts import render

# 부트스트랩 : https://startbootstrap.com/template/sb-admin
# 대쉬보드1의 차트 : https://www.highcharts.com/demo/line-labels

# Create your views here.
def home(request):
	data = []
	for i in range(1, 100):
		person = {}
		person['name'] = 'james' + str(i)
		person['position'] = 'position' + str(i)
		person['office'] = 'office' + str(i)
		person['age'] = i
		person['salary'] = i * 1000
		person['date'] = time.ctime()
		data.append(person)

	context = {
		'section': 'main_section.html',
		'persons': data,
	}
	return render(request, 'index.html', context)

def dashboard1(request):
	context = {
		'section': 'dashboard1.html'
	}
	return render(request, 'index.html', context)

def dashboard2(request):
	context = {
		'section': 'dashboard2.html'
	}
	return render(request, 'index.html', context)

def dashboard3(request):
	context = {
		'section': 'dashboard3.html'
	}
	return render(request, 'index.html', context)

def tabledata(request):
	data = []
	for i in range(1, 100):
		person = {}
		person['name'] = 'james' + str(i)
		person['position'] = 'position' + str(i)
		person['office'] = 'office' + str(i)
		person['age'] = i
		person['salary'] = i * 1000
		person['date'] = time.ctime()
		data.append(person)

	return HttpResponse(json.dumps(data), content_type='application/json')

def chart1(request):
	data = [
		{'name': 'Tokyo', 'data': [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]},
		{'name': 'London', 'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]}
	]
	return HttpResponse(json.dumps(data), content_type='application/json')