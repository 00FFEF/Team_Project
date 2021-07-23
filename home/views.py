from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, 'index.html')

def scrapping_index(request):
    return render(request,'scrapping_index.html')

def machine_index(request):
    return render(request,'machine_index.html')

def service_index(request):
    return render(request,'service_index.html')