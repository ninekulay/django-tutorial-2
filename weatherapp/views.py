from django.shortcuts import render , redirect
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=67e025faa238a84edb76a6dddf75f693'
    city = 'Bangkok'
    if request.method == "POST":
        data = request.POST.copy()
        city = data.get('city_name')
        if city == '' :
            city = 'Bangkok'
    response = requests.get(url.format(city)).json()
    city_weather = {
        'city' : city,
        'temperature' : response['main']['temp'],
        'description' : response['weather'][0]['description'],
        'icon' : response['weather'][0]['icon']
    }
    context = {'city_weather' : city_weather}
    return render(request, 'weather/weather.html',context)