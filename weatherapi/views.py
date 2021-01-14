import requests
from django.shortcuts import render
from .models import APIKey
from .cities import cities

def IndexView(request):
    if request.method == 'POST':
        city = request.POST['city']
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + f'{APIKey.objects.get(id=1).key}').json()
        context = {
            "city": city.title(),
            "kelvin": str(response['main']['temp']),
            "celsius": str(response['main']['temp'] - 273.15),
            "postmethod": True,
            "cities": cities,
        }
    else:
        context = {}
    return render(request, "weatherapi/index.html", context)