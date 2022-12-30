from django.shortcuts import render,HttpResponse
import requests

# Create your views here.

def index(request):
    result= requests.get('https://api.covid19api.com/summary')
    json=result.json()
    GlobalData=json['Global']
    countrywise=json['Countries']
    print(countrywise)
    return render(request, 'index.html',{'GlobalData':GlobalData, 'countrywise':countrywise})
    
    