from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    path = request.path
    resultstr = ''
    if path == '/home':
        resultstr = '<h1>여기는 home입니다.</h1>'
    else:
        resultstr = '<h1>여기는 main 입니다.</h1>'

    return HttpResponse(resultstr)

def index01(request):
    result = {'first':'Team Name', 'second':'Phoenix'}
    return render(request, 'index.html', context=result)