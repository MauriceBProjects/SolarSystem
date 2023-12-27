from django.shortcuts import render
from .models import Planet

def home(request):
    planets = Planet.objects.all()
    return render(request, 'home.html', {'planets':planets})
