from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

# b=[{'city':0}]
def home(request):
    return render(request,'base/home.html')

def city(request):
    if request.method=="POST":
        d=dict(request.POST)
        a=''.join(d['city'])
        inte=''.join(d['numberofdays'])
        st="https://api.weatherapi.com/v1/forecast.json?key=5b79b1cb7bd842dc9e9200012231106&q={city}&days={numberofdays}&aqi=no&alerts=no"
        s=st.format(city=a,numberofdays=inte)
        response=requests.get(s)
        res=response.json()
        room=[]
        for i in range(int(inte)):
            e={"location":res['location']['name'],"date":res['forecast']['forecastday'][i]['date'],"maxtemp_c":res['forecast']['forecastday'][i]['day']['maxtemp_c'],"mintemp_c":res['forecast']['forecastday'][i]['day']['mintemp_c'],"avgtemp_c":res['forecast']['forecastday'][i]['day']['avgtemp_c'],"sunrise":res['forecast']['forecastday'][i]['astro']['sunrise'],"sunset":res['forecast']['forecastday'][i]['astro']['sunset'],'moonphase':res['forecast']['forecastday'][i]['astro']['moon_phase'],"condition":res['forecast']['forecastday'][i]['day']['condition']['text'],"windspeed":res['forecast']['forecastday'][i]['day']['maxwind_kph'],"pic":res['forecast']['forecastday'][i]['day']['condition']['icon'],"days":int(inte),"dat":i}
            room.append(e)
        context={"room":room}
        return render(request,'base/city.html',context)
        
    
def date(request,city,date,days):
    st="https://api.weatherapi.com/v1/forecast.json?key=5b79b1cb7bd842dc9e9200012231106&q={city}&days={numberofdays}&aqi=no&alerts=no"
    s=st.format(city=city,numberofdays=days)
    res=requests.get(s).json()
    room=[]
    d=int(date)
    for i in range(24):
        print(i)
        e={"hour":res['forecast']['forecastday'][d]['hour'][i]['time'],"temp_c":res['forecast']['forecastday'][d]['hour'][i]['temp_c'],"condition":res['forecast']['forecastday'][d]['hour'][i]['condition']['text'],"icon":res['forecast']['forecastday'][d]['hour'][i]['condition']['icon']}
        room.append(e)
    context={"room":room}
    return render (request,'base/date.html',context)
