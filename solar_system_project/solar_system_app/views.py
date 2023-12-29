from django.shortcuts import render
from .models import Planet

def home(request):
    planets = Planet.objects.all()
    for planet in planets:
        planet.radius_class = get_radius_class(planet.radius)
        print(planet.radius)
    return render(request, 'home.html', {'planets':planets})


def get_radius_class(radius):
    if radius < 10:
        return 'small'
    elif 10 <= radius <= 20:
        return 'medium'
    else: 
        return 'large'