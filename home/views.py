import json
from django.shortcuts import render
from django.http import HttpResponse
from templates.MyAnalysis import MyAnalysis

# Create your views here.
def main(request):
    return render(request, 'index.html')

def scrapping_index(request):
    return render(request,'scrapping_index.html')

def machine_index(request):
    return render(request,'machine_index.html')

def service_index(request):
    return render(request,'service_index.html')

def kakao_chart(request):
    data = MyAnalysis().kakaoo()
    return HttpResponse(json.dumps(data), content_type='application/json')

def naver_chart(request):
    data = MyAnalysis().never()
    return HttpResponse(json.dumps(data), content_type='application/json')