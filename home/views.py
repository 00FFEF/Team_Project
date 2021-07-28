import json
from django.shortcuts import render
from django.http import HttpResponse
from templates.MyAnalysis import MyAnalysis
import sqlite3

# Create your views here.
def main(request):
    return render(request, 'index.html')

def scrapping_index(request):
    return render(request,'scrapping_index.html')

def machine_index(request):
    result = dict()
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row  # for getting columns
    curs = conn.cursor()
    curs.execute('select * from dbapp_admachine da')
    data = curs.fetchall()
    for row in data:
        print(row['Age'])
        print(row['EstimatedSalary'])
        print(row['Gender'])
        print(row['Purchased'])
        print(row['UserID'])
        print(row['id'])
    result['erows'] = data

    return render(request,'machine_index.html',result)

def service_index(request):
    return render(request,'service_index.html')

def kakao_chart(request):
    data = MyAnalysis().kakaoo()
    return HttpResponse(json.dumps(data), content_type='application/json')

def naver_chart(request):
    data = MyAnalysis().never()
    return HttpResponse(json.dumps(data), content_type='application/json')