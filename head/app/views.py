from django.shortcuts import render, HttpResponse, redirect
from app.models import Place, Nearby
import random

# Create your views here.
def test(request):
    placesall = Place.objects.all()
    places = Place.objects.all()[:3]
    rand_places = []

    for i in range(3):
        rand_place = rand_places.append(random.choice(placesall))

    print(rand_places)

    context = {
        "places": places,
        "rand1": rand_places[0],
        "rand2": rand_places[1],
        "rand3": rand_places[2],
    }

    return render(request, 'index.html', context)

def all(request):
    places = Place.objects.all()
    rand_places = []

    for i in range(3):
        rand_place = rand_places.append(random.choice(places))

    context = {
        "places": places,
        "rand1": rand_places[0],
        "rand2": rand_places[1],
        "rand3": rand_places[2],
    }

    return render(request, 'all.html', context)

def place(request, place_id):
    placesall = Place.objects.all()[:3]
    rand_places = []

    for i in range(3):
        rand_place = rand_places.append(random.choice(placesall))

    places = Place.objects.filter(place_id=place_id)
    nearby = Nearby.objects.filter(fk=places[0])

    context = {
        "places": places,
        "nearby": nearby,
        "rand1": rand_places[0],
        "rand2": rand_places[1],
        "rand3": rand_places[2]
    }

    return render(request, "place.html", context)

def nearby(request, nearby):
    places = Nearby.objects.filter(nearby_id=nearby)[:3]

    context = {
        "places": places
    }

    return render(request, "place.html", context)

def search(request, name):
    places = Place.objects.filter(name__contains=name)

    context = {
        "places": places
    }

    return render(request, "search.html", context)